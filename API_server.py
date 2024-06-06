from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
load_dotenv()
username = os.getenv("USERNAME")
userpassword = os.getenv("USERPASSWORD")
host = os.getenv("VITE_APP_HOST")
port = os.getenv("PORT")
database = os.getenv("DBNAME")

# Инициализация подключения к базе данных с помощью SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{username}:{userpassword}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  
db = SQLAlchemy(app)  # Инициализация экземпляра SQLAlchemy

# Модель для таблицы "satellites"
class Satellite(db.Model):
    __tablename__ = 'satellites'
    satellite_name = db.Column(db.String, primary_key=True)
    arg_perigee = db.Column(db.String)
    bstar = db.Column(db.String)
    checksum = db.Column(db.String)
    checksum_2 = db.Column(db.String)
    classification = db.Column(db.String)
    eccentricity = db.Column(db.String)
    element_set_number = db.Column(db.String)
    ephemeris_type = db.Column(db.String)
    epoch = db.Column(db.String)
    epoch_year = db.Column(db.String)
    inclination = db.Column(db.String)
    iss_number = db.Column(db.String)
    launch_fragment = db.Column(db.String)
    launch_number = db.Column(db.String)
    launch_year = db.Column(db.String)
    line1 = db.Column(db.String)
    line2 = db.Column(db.String)
    mean_anomaly = db.Column(db.String)
    mean_motion = db.Column(db.String)
    mean_motion_derivative = db.Column(db.String)
    orbit_number = db.Column(db.String)
    raan = db.Column(db.String)
    second_derivative = db.Column(db.String)

    def serialize(self):
        return {
            'satellite_name': self.satellite_name,
            'arg_perigee': self.arg_perigee,
            'bstar': self.bstar,
            'checksum': self.checksum,
            'checksum_2': self.checksum_2,
            'classification': self.classification,
            'eccentricity': self.eccentricity,
            'element_set_number': self.element_set_number,
            'ephemeris_type': self.ephemeris_type,
            'epoch': self.epoch,
            'epoch_year': self.epoch_year,
            'inclination': self.inclination,
            'iss_number': self.iss_number,
            'launch_fragment': self.launch_fragment,
            'launch_number': self.launch_number,
            'launch_year': self.launch_year,
            'line1': self.line1,
            'line2': self.line2,
            'mean_anomaly': self.mean_anomaly,
            'mean_motion': self.mean_motion,
            'mean_motion_derivative': self.mean_motion_derivative,
            'orbit_number': self.orbit_number,
            'raan': self.raan,
            'second_derivative': self.second_derivative
        }

# Функция для извлечения данных из таблицы "satellites"
@app.route('/api/data', methods=['GET'])
def get_data():
   try:
       data = Satellite.query.all()  # Использование SQLAlchemy для выборки всех данных из таблицы "satellites"
       result = [item.serialize() for item in data]  # Преобразование объектов Satellite в формат JSON
       return jsonify(result)  # Возврат JSON-представления результатов
   except Exception as e:  # Обработка общего исключения
       return jsonify({"error": f"Failed to retrieve data: {e}"})

# Запуск веб-приложения
if __name__ == '__main__':
    app.run(host=host, port=3000)

