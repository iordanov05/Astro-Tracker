from flask import Flask, jsonify, request
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)


load_dotenv()
username = os.getenv("USERNAME")
userpassword = os.getenv("USERPASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
database = os.getenv("DBNAME")
try:
    connection = psycopg2.connect(
        user=username,
        password=userpassword,
        host=host,
        port=port,
        database=database
    )
    cursor = connection.cursor()
except Error as e:
    print(f"Error connecting to PostgreSQL database: {e}")

# Пример эндпоинта для получения данных
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        cursor.execute("SELECT * FROM satellites")
        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        result = []
        for row in data:
            row_data = {}
            for i in range(len(column_names)):
                row_data[column_names[i]] = row[i]
            result.append(row_data)

        return jsonify(result)
    except Error as e:
        return jsonify({"error": f"Failed to retrieve data: {e}"})


app.run(host=host, port=3000)