import requests
import textwrap

url = "https://r4uab.ru/satonline.txt"

response = requests.get(url)

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
        
        satellite = (f'"""{group}\n"""')
        print(satellite)
        grouped_lines_array.append(textwrap.dedent(satellite).strip())
        
    
else:
    print("Ошибка при получении данных:", response.status_code)
