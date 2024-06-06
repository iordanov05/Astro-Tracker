import asyncio
import websockets
import json
from skyfield.api import Loader, EarthSatellite
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2
from dotenv import load_dotenv
import os
load_dotenv()
host = os.getenv("VITE_APP_HOST")
print("Server started")    
    
def coordinateСalculation(line1, line2, satellite_name, year, month, day, hour, minute, second):
# Загрузка данных о спутниках
    load = Loader('~/skyfield-data')
    ts = load.timescale()
    satellite = EarthSatellite(line1, line2, satellite_name, ts)
    t = ts.utc(year, month, day, hour, minute, second)

# Получение положения спутника на текущее время
    geometry = satellite.at(t)
    subpoint = geometry.subpoint()

# Вывод координат местоположения спутника
    latitude = subpoint.latitude.degrees
    longitude = subpoint.longitude.degrees
    altitude = subpoint.elevation.m

    return ("{:.4f}".format(latitude),"{:.4f}".format(longitude),"{:.2f}".format(altitude/1000))



def calculatDistance(placeLatitude,placeLongitude,satelliteLatitude,satelliteLongitude,satelliteHeight):
    R = 6371  
    R += satelliteHeight / 1000
    placeLatitude, placeLongitude, satelliteLatitude, satelliteLongitude = map(radians, [placeLatitude, placeLongitude, satelliteLatitude, satelliteLongitude])

    dlat = satelliteLatitude - placeLatitude
    dlon = satelliteLongitude - placeLongitude

    a = sin(dlat/2)**2 + cos(placeLatitude) * cos(satelliteLatitude) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    distance = round(distance, 2)
    return distance

from datetime import datetime, timedelta

def trackGeneration(line1, line2, satellite_name):
    track = []
    now = datetime.now()
    now -= timedelta(hours=1)
    for i in range(120):
        x, y, _ = coordinateСalculation(line1, line2, satellite_name, now.year, now.month, now.day, now.hour, now.minute, now.second)
        track.append({'x': x, 'y': y})
        now += timedelta(minutes=1)  

    return track


async def send_data(websocket):
    print("Connection established")
    
    try:
        data_str = await websocket.recv()

        data_dict = json.loads(data_str)
        selectedSatellite = None
        placeLongitude = None
        placeLatitude = None
        while True:
            satelliteTrack = None
            for satellite in data_dict:
                
                if isinstance(satellite.get("track"), str):
                    satelliteTrack = satellite["track"]
                
                if satellite.get("sat_name") is not None:
                    selectedSatellite = satellite["sat_name"]
                    placeLongitude = satellite["longitude"]
                    placeLatitude = satellite["latitude"]
                
                if satellite.get("satellite_name"):
                    now = datetime.now()
                    satellite["latitude"],satellite["longitude"],satellite["height"]  = coordinateСalculation(satellite["line_1"],satellite["line_2"],satellite["satellite_name"],now.year, now.month, now.day, now.hour, now.minute, now.second)
                    
                    if selectedSatellite is not None:
     
                        if satellite["satellite_name"] == selectedSatellite:
                            data_dict[0]["distance"] = calculatDistance(float(placeLatitude), float(placeLongitude), float(satellite["latitude"]), float(satellite["longitude"]), float(satellite["height"]))
                    
                    if satelliteTrack is not None: 
                      
                        if satellite["satellite_name"] == satelliteTrack:
                            data_dict[0]["track"] = trackGeneration(satellite["line_1"],satellite["line_2"],satellite["satellite_name"])
                            
            await websocket.send(json.dumps(data_dict))
            print(len(data_dict))
            await asyncio.sleep(5)
            

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Client disconnected with error code {e.code}: {e.reason}")

    except websockets.exceptions.ConnectionClosedOK as e:
        print("Client disconnected gracefully.")

start_server = websockets.serve(send_data,host, 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
