import schedule
import time
import os

def run_script():
    os.system('python tle.py')
    os.system('python tle_decoder.py')
    os.system('python database_creation.py')
    

# Запуск скрипта в 14:00 каждый день
schedule.every().day.at("14:00").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(60)  # Проверка расписания каждую минуту
