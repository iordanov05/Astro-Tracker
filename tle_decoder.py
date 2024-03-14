from datetime import datetime, timedelta
from tle import grouped_lines_array
current_year = datetime.now().year # Определение текущего года

# Функция для преобразования эпохи в дату и время
def convert_epoch_to_date(epoch):
    day_of_year = int(epoch.split('.')[0])
    fraction_of_day = float("0." + epoch.split('.')[1])

    current_year = datetime.now().year
    epoch_date = datetime(year=current_year, month=1, day=1) + timedelta(days=day_of_year) + timedelta(seconds=fraction_of_day*24*60*60)
    formatted_date = epoch_date.strftime("%d.%m.%Y")
    formatted_time = epoch_date.strftime("%H:%M:%S")
    return f"{formatted_date}, {formatted_time}"

# Функция для вычисления контрольной суммы
def compute_checksum(tle_line):
    summ=''
    print(tle_line)
    tle_line = tle_line.rstrip(' ')
    tle_line = tle_line[:-1]
    for i in tle_line:
        if i.isdigit()==0 and i != "-":
            tle_line = tle_line.replace(i, '0')
        elif i == "-":
            tle_line = tle_line.replace(i, '1')
    summ = str(sum(list(map(int, tle_line.strip()))))[-1]
    return summ

# Функция для разбора TLE 
def parse_tle(tle_text):
    t_lines = tle_text.split('\n')
    satellite_name = t_lines[0].strip()
    line1 = t_lines[1]
    line2 = t_lines[2]
    satellite_data = {
        "Спутник": satellite_name.lstrip('"'),
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
            "Контрольная сумма": str(f"{line1[68]} - Контрольная сумма верна!" if compute_checksum(line1) == line1[68] else 	f"{line1[68]} - Неверная контрольная сумма!"), 
        },
        "Строка 2": {
            "Наклонение, i": line2[8:16],
            "Прямое восхождение восходящего узла, Ω": line2[17:25],
            "Эксцентриситет, e": f"0.{line2[26:33]}",
            "Аргумент перигея, ω": line2[34:42],
            "Средняя аномалия, ν": line2[43:51],
            
            "Среднее движение [оборотов в день]": line2[52:63],
            "Номер витка": line2[63:68], 
            "Контрольная сумма": str(f"{line2[68]} - Контрольная сумма верна!" if compute_checksum(line2) == line2[68] else f"{line2[68]} - Неверная контрольная сумма!"),
        }
    }

    return satellite_data

array_of_parsed_tle_array = []

# Цикл для обработки массива TLE строк
for tle_data in grouped_lines_array:
    parsed_tle_array = []
    parsed_tle = parse_tle(tle_data)
    for key, value in parsed_tle.items():
        if isinstance(value, dict):
            sub_values = list(value.values())
            parsed_tle_array.extend(sub_values)
        else:
            parsed_tle_array.append(value)
    array_of_parsed_tle_array.append(parsed_tle_array)
   
# Сортировка массива рассчитанных TLE данных 
array_of_parsed_tle_array = sorted(array_of_parsed_tle_array, key=lambda x: x[0])

# Вывод статуса декодирования
print("Decoding status:", True)