import psycopg2
from tle_decoder import array_of_parsed_tle_array
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("USERNAME")
userpassword = os.getenv("USERPASSWORD")
database = os.getenv("DBNAME")
host = os.getenv("HOST")
port = os.getenv("PORT")

conn = psycopg2.connect(
    user=username,
    password=userpassword,
    dbname=database,
    host=host,
    port=port
)

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS satellites (
        satellite_name VARCHAR(255),
        iss_number VARCHAR(100),
        classification VARCHAR(100),
        launch_year VARCHAR(100),
        launch_number VARCHAR(100),
        launch_fragment VARCHAR(100),
        epoch_year VARCHAR(100),
        epoch VARCHAR(100),
        mean_motion_derivative VARCHAR(100),
        second_derivative VARCHAR(100),
        bstar VARCHAR(100),
        ephemeris_type VARCHAR(100),
        element_set_number VARCHAR(100),
        checksum VARCHAR(100),
        inclination VARCHAR(100),
        raan VARCHAR(100),
        eccentricity VARCHAR(100),
        arg_perigee VARCHAR(100),
        mean_anomaly VARCHAR(100),
        mean_motion VARCHAR(100),
        orbit_number VARCHAR(100),
        checksum_2 VARCHAR(100)
    );
    TRUNCATE TABLE satellites; 

''')
for element_of_array in array_of_parsed_tle_array:
    satellite_data = {
        "satellite_name": element_of_array[0],
        "iss_number": (element_of_array[1]),
        "classification": element_of_array[2],
        "launch_year": (element_of_array[3]),
        "launch_number": (element_of_array[4]),
        "launch_fragment": element_of_array[5],
        "epoch_year": (element_of_array[6]),
        "epoch": element_of_array[7],
        "mean_motion_derivative": element_of_array[8],
        "second_derivative": element_of_array[9],
        "bstar": element_of_array[10],
        "ephemeris_type": element_of_array[11],
        "element_set_number": (element_of_array[12]),
        "checksum": element_of_array[13],
        "inclination": element_of_array[14],
        "raan": element_of_array[15],
        "eccentricity": element_of_array[16],
        "arg_perigee": element_of_array[17],
        "mean_anomaly": element_of_array[18],
        "mean_motion": element_of_array[19],
        "orbit_number": (element_of_array[20]),
        "checksum_2": element_of_array[21]
    }

    cur.execute('''
        INSERT INTO satellites (satellite_name, iss_number, classification, launch_year, launch_number, launch_fragment, epoch_year, 
                                epoch, mean_motion_derivative, second_derivative, bstar, ephemeris_type, element_set_number, checksum,
                                inclination, raan, eccentricity, arg_perigee, mean_anomaly, mean_motion, orbit_number, checksum_2)
        VALUES (%(satellite_name)s, %(iss_number)s, %(classification)s, %(launch_year)s, %(launch_number)s, %(launch_fragment)s, %(epoch_year)s, 
                %(epoch)s, %(mean_motion_derivative)s, %(second_derivative)s, %(bstar)s, %(ephemeris_type)s, %(element_set_number)s, %(checksum)s,
                %(inclination)s, %(raan)s, %(eccentricity)s, %(arg_perigee)s, %(mean_anomaly)s, %(mean_motion)s, %(orbit_number)s, %(checksum_2)s);
    ''', satellite_data)

conn.commit()
cur.close()
conn.close()