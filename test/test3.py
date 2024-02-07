
import logging
from pytz import timezone 
from datetime import datetime
import time

import threading


#########################################################
logging.basicConfig(level=logging.INFO, filename='test/test3.log', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding = 'utf-8', filemode='w')

warlock = logging.getLogger(__name__)
handler = logging.FileHandler('warlock.log', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')


tz = timezone('Etc/GMT+0') # UTC + 3
formatter.converter = lambda *args: tz.fromutc(datetime.utcnow()).timetuple()

handler.setFormatter(formatter)


warlock.addHandler(handler)
############################################################


while True:
    time.sleep(5)
    print(tz)
    warlock.info('45423')

