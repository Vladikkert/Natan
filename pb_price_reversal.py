
import websocket
import json
import time
import pickle

import logging
from pytz import timezone 
from datetime import datetime

import threading


#########################################################
logging.basicConfig(level=logging.INFO, filename='pb_price_reversal.log', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                    encoding = 'utf-8', filemode='w')

warlock = logging.getLogger(__name__)
handler = logging.FileHandler('warlock.log', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')


tz = timezone('Europe/Moscow') # UTC + 3
formatter.converter = lambda *args: tz.fromutc(datetime.utcnow()).timetuple()

handler.setFormatter(formatter)


warlock.addHandler(handler)
############################################################



def update_last_price():

    file2 = open(f"za_last_price_5.pkl", "rb")
    last_price_5 = pickle.load(file2)
    file2.close()

    file3 = open(f"za_last_price_sma.pkl", "rb")
    last_price_sma = pickle.load(file3)
    file3.close()
 
    # file3 = open(f"za_last_price_rsi.pkl", "rb")
    # last_price_rsi = pickle.load(file3)
    # file3.close()

    
    # # Обновляем значения в словаре

    for key in last_price_5.keys():
       
        last_price_5_eq = last_price_5[key][-6000:]
        last_price_sma_eq = last_price_sma[key][-6000:]
        if key == 'BTCUSDT': 
            print(len(last_price_sma_eq))
            print(1)
        if len(last_price_sma_eq) < 5999:
            print(key)
            break

        now_price = last_price_5_eq[-1]
        now_sma = last_price_sma_eq[-1]


        all_persent_change = []
        for price, sma in zip(last_price_5_eq, last_price_sma_eq):
            x = abs(price - sma)/sma * 100
            all_persent_change.append(x)

        average_deviation = sum(all_persent_change)/len(all_persent_change)

        if abs(now_price - now_sma)/sma > 5:
            if abs(now_price - now_sma)/sma * 100 > average_deviation * 10:
                warlock.critical(f'{key}, {abs(now_price - now_sma)/sma * 100}, {average_deviation}, {now_price}')
                file3 = open(f"za_pop_coin.pkl", "wb")
                pickle.dump([key, now_sma, now_price], file3)
                file3.close()

        #print(1)


            
    # Сохраняем обновленный словарь по 5 тысячам монет в новый фай



warlock.info('*****НАХОДИМ РАСТУЩУЮ МОНЕТУ*****')

while True:
    try:
        update_last_price()
    except Exception as e:
        warlock.error('*****СБОЙ ПОИСКА РАСТУЩЕЙ МОНЕТЫ, ПЕРЕПОДКЛЮЧЕНИЕ*****')
        time.sleep(2)
        continue

    #l = load('za_last_price_5')
    #print(l['BTCUSDT'])
    time.sleep(2)
