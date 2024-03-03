from datetime import datetime, timedelta
current_year = datetime.now().year

def convert_epoch_to_date(epoch):
    day_of_year = int(epoch.split('.')[0])
    fraction_of_day = float("0." + epoch.split('.')[1])

    current_year = datetime.now().year
    epoch_date = datetime(year=current_year, month=1, day=1) + timedelta(days=day_of_year) + timedelta(seconds=fraction_of_day*24*60*60)
    formatted_date = epoch_date.strftime("%d.%m.%Y")
    formatted_time = epoch_date.strftime("%H:%M:%S")
    return f"{formatted_date}, {formatted_time}"


def parse_tle(tle_text):
    t_lines = tle_text.split('\n')
    satellite_name = t_lines[0].strip()
    line1 = t_lines[1]
    line2 = t_lines[2]
    satellite_data = {
        "Спутник": satellite_name,
        "Строка 1": {
            "Номер ИСЗ": line1[2:7],
            "Классификация": line1[7],
            "Год запуска": str(int(line1[9:11]) + 1900 if int(line1[9:11]) > current_year - 2000 else int(line1[9:11]) + 2000),
            "Номер запуска в году": line1[11:14].lstrip('0'),
            "Фрагмент запуска": line1[14:17],
            "Год эпохи": str(int(line1[18:20]) + 1900 if int(line1[18:20]) > current_year - 2000 else int(line1[18:20]) + 2000),
            "Эпоха": convert_epoch_to_date(line1[20:32]), 
            "Первая производная среднего движения по времени": line1[33:43],
            "Вторая производная среднего движения по времени": line1[45:52],
            "Коэффициент торможения (BSTAR)": line1[53:61],
            "Тип эфемериды (орбитальная модель)": "SGP4/SDP4 (default)", 
            "Номер набора элементов": line1[63:68],
            "Контрольная сумма": line1[68]
        },
        "Строка 2": {
            "Номер ИСЗ": line2[2:7],
            "Наклонение, i": line2[8:16],
            "Прямое восхождение восходящего узла, Ω": line2[17:25],
            "Эксцентриситет, e": f"0.{line2[26:33]}",
            "Аргумент перигея, ω": line2[34:42],
            "Средняя аномалия, ν": line2[43:51],
            
            "Среднее движение [оборотов в день]": line2[52:63],
            "Номер витка": line2[63:68], 
            "Контрольная сумма":line2[68] 
        }
    }

    return satellite_data
tle_data = """SITRO-AIS-6 (CHIRKIN)
1 57192U 23091AC  24061.87562790  .00006122  00000-0  41742-3 0  9998
2 57192  97.6293 115.0895 0019494 125.2711 235.0344 15.06449074 37334
"""
parsed_tle = parse_tle(tle_data)

    
for key, value in parsed_tle.items():
    print(key + ":")
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print(f"   {sub_key}: {sub_value}")
    else:
        print(f"   {value}")
    print()