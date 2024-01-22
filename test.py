import websocket
import pickle
import json

#Функция загрузки из файла
def load(file):
    with open(f'{file}.pkl', 'rb') as f:
        data = pickle.load(f)
    return data

#Функция записи в файл
def dump(file, data):
    with open(f'{file}.pkl', 'wb') as f:
        pickle.dump(data, f)

dump('za_last_price_rsi', {})

#dump('za_last_price_5', {})

# a = load('za_last_price_5')

# value = a.pop("ETHUSDT_240628")

# dump('za_last_price', value)




