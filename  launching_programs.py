import schedule  # Импорт модуля для работы с расписанием
import time  # Импорт модуля для работы с временем
import os  # Импорт модуля для работы с операционной системой

def run_script():
   os.system('python tle.py')  # Запуск скрипта tle.py
   os.system('python tle_decoder.py')  # Запуск скрипта tle_decoder.py
   os.system('python database_creation.py')  # Запуск скрипта database_creation.py

schedule.every().day.at("14:00").do(run_script)  # Запуск run_script в 14:00 каждый день

while True:
   schedule.run_pending()  # Проверка и выполнение запланированных задач
   time.sleep(60)  # Пауза в 60 секунд для проверки расписания каждую минуту
