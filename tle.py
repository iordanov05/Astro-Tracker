import requests

url = "https://r4uab.ru/satonline.txt"

response = requests.get(url)

if response.status_code == 200:
    data = response.text
    
    print(data)
    
else:
    print("Ошибка при получении данных:", response.status_code)
