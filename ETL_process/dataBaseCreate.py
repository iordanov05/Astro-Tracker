import psycopg2 # Импорт библиотеки psycopg2 для подключения к PostgreSQL.
from decoderData import array_of_parsed_tle_array # Импорт переменной array_of_parsed_tle_array из модуля tle_decoder.
from dotenv import load_dotenv # Импорт модуля для загрузки переменных среды из файла .env.
import os # Импорт модуля для работы с операционной системой.


try:
   print('go')
   # Загрузка переменных окружения из файла .env
   load_dotenv()
   username = os.getenv("USERNAME")
   userpassword = os.getenv("USERPASSWORD")
   database = os.getenv("DBNAME")
   host = os.getenv("VITE_APP_HOST")
   port = os.getenv("PORT")

   # Подключение к базе данных PostgreSQL
   conn = psycopg2.connect(
       user=username,
       password=userpassword,
       dbname=database,
       host=host,
       port=port
   )

   # Создание объекта курсора с использованием соединения
   cur = conn.cursor()

   # Создание таблицы, если она не существует, и очистка таблицы
   cur.execute('''
        DROP TABLE IF EXISTS satellites;  -- Удаляем таблицу, если она уже существует
   CREATE TABLE satellites (
       satellite_name VARCHAR(255),
       line1 VARCHAR(255),
       line2 VARCHAR(255),
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
''')
   # Перебор элементов разобранного массива TLE и вставка данных в таблицу PostgreSQL
   for element_of_array in array_of_parsed_tle_array:
       satellite_data = {
           "satellite_name": element_of_array[0],
           "line1": element_of_array[1],
           "line2": element_of_array[2],
           "iss_number": element_of_array[3],
           "classification": element_of_array[4],
           "launch_year": element_of_array[5],
           "launch_number": element_of_array[6],
           "launch_fragment": element_of_array[7],
           "epoch_year": element_of_array[8],
           "epoch": element_of_array[9],
           "mean_motion_derivative": element_of_array[10],
           "second_derivative": element_of_array[11],
           "bstar": element_of_array[12],
           "ephemeris_type": element_of_array[13],
           "element_set_number": element_of_array[14],
           "checksum": element_of_array[15],
           "inclination": element_of_array[16],
           "raan": element_of_array[17],
           "eccentricity": element_of_array[18],
           "arg_perigee": element_of_array[19],
           "mean_anomaly": element_of_array[20],
           "mean_motion": element_of_array[21],
           "orbit_number": element_of_array[22],
           "checksum_2": element_of_array[23]
       }

       # Вставка данных в таблицу PostgreSQL
       cur.execute('''
           INSERT INTO satellites (satellite_name, line1, line2, iss_number, classification, launch_year, launch_number, launch_fragment, epoch_year, 
                                   epoch, mean_motion_derivative, second_derivative, bstar, ephemeris_type, element_set_number, checksum,
                                   inclination, raan, eccentricity, arg_perigee, mean_anomaly, mean_motion, orbit_number, checksum_2)
           VALUES (%(satellite_name)s, %(line1)s, %(line2)s, %(iss_number)s, %(classification)s, %(launch_year)s, %(launch_number)s, %(launch_fragment)s, %(epoch_year)s, 
                   %(epoch)s, %(mean_motion_derivative)s, %(second_derivative)s, %(bstar)s, %(ephemeris_type)s, %(element_set_number)s, %(checksum)s,
                   %(inclination)s, %(raan)s, %(eccentricity)s, %(arg_perigee)s, %(mean_anomaly)s, %(mean_motion)s, %(orbit_number)s, %(checksum_2)s);
       ''', satellite_data)
   # Фиксация изменений в базе данных
   conn.commit()
   # Закрытие объекта курсора и соединения
   cur.close()
   conn.close()
   # Вывод статуса отправки при успешном завершении
   print("Submission status:", True)

except psycopg2.DatabaseError as e:
    print(f"Error connecting to the database: {e}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")