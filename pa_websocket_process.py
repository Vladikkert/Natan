import subprocess
import time

import logging
from pytz import timezone 
from datetime import datetime

#########################################################
logging.basicConfig(level=logging.INFO, filename='pa_websocket_process_logging.log', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding = 'utf-8', filemode='w')

warlock = logging.getLogger(__name__)
handler = logging.FileHandler('warlock.log', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')


tz = timezone('Europe/Moscow') # UTC + 3
formatter.converter = lambda *args: tz.fromutc(datetime.utcnow()).timetuple()

handler.setFormatter(formatter)


warlock.addHandler(handler)
############################################################



i = 0
while True:
    warlock.info('*****Стартуем!!*****')
    process = subprocess.Popen(['/bin/python3.10', 'pa_websocket.py'])
    process.wait()
    if process.returncode == 0:  # Если процесс завершился успешно, выходим из цикла
        i = i + 1
        warlock.error("Процесс завершился неудачно, перезапуск через 1 минуту...", 'перезапущено ', i, 'раз')
        time.sleep(3)  # Пауза в 15 секунд перед следующим запуском                 