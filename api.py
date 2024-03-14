from flask import Flask, jsonify, request  # Импорт необходимых модулей Flask для создания веб-приложения
import psycopg2  # Импорт модуля для работы с базой данных PostgreSQL
from psycopg2 import Error  # Импорт обработчика ошибок модуля psycopg2
from dotenv import load_dotenv  # Импорт модуля для загрузки переменных среды из файла .env
import os  # Импорт модуля для работы с операционной системой
from flask_cors import CORS  # Импорт модуля для обеспечения CORS в приложении Flask

app = Flask(__name__)  # Создание экземпляра Flask-приложения
CORS(app)  # Включение обработки CORS в приложении

load_dotenv()  # Загрузка переменных среды из файла .env
username = os.getenv("USERNAME")  
userpassword = os.getenv("USERPASSWORD")  
host = os.getenv("HOST")  
port = os.getenv("PORT")  
database = os.getenv("DBNAME") 
try:
   connection = psycopg2.connect(  # Подключение к базе данных PostgreSQL
       user=username,
       password=userpassword,
       host=host,
       port=port,
       database=database
   )
   cursor = connection.cursor()  # Создание курсора для выполнения запросов к базе данных
except Error as e:
   print(f"Error connecting to PostgreSQL database: {e}")  # Вывод сообщения об ошибке при подключении к базе данных


@app.route('/api/data', methods=['GET'])
def get_data():
   try:
       cursor.execute("SELECT * FROM satellites")  # Выполнение SQL-запроса для выборки данных из таблицы "satellites"
       data = cursor.fetchall()  # Получение всех выбранных данных
       column_names = [desc[0] for desc in cursor.description]  # Получение названий столбцов результирующего набора

       result = []  # Инициализация списка для хранения результатов
       for row in data:
           row_data = {}
           for i in range(len(column_names)):
               row_data[column_names[i]] = row[i]  # Создание словаря с данными каждой строки
           result.append(row_data)  # Добавление словаря в список результатов

       return jsonify(result)  # Возврат JSON-представления результатов
   except Error as e:
       return jsonify({"error": f"Failed to retrieve data: {e}"}) 
app.run(host=host, port=3000)  # Запуск веб-приложения на указанном хосте и порту
