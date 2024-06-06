import requests
import textwrap

def get_all_satellite_data(format_type='TLE'):
    base_url = 'https://celestrak.org/NORAD/elements/gp.php'
    params = {'QUERY': 'GROUP', 'GROUP': 'ACTIVE', 'FORMAT': format_type}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.text

        # Разделим данные на строки
        lines = data.strip().split('\n')

        # Объединим каждую группу из трех строк в одну строку
        grouped_lines = [lines[i] + '\n' + lines[i+1] + '\n' + lines[i+2] for i in range(0, len(lines), 3)]

        # Создаем пустой список для хранения групп строк
        grouped_lines_array = []

        # Добавим каждую строку в массив с сохранением форматирования
        for group in grouped_lines:
            satellite = f'"""{group}\n"""'
            grouped_lines_array.append(textwrap.dedent(satellite).strip())

        return grouped_lines_array
    else:
        print("Ошибка при получении данных:", response.status_code)
        return []


data_format = 'TLE'  

celestrak_data = get_all_satellite_data(data_format)
