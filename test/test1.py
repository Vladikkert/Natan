import websocket
import pickle
import json
import time

#Функция загрузки из файла
def load(file):
    with open(f'{file}.pkl', 'rb') as f:
        data = pickle.load(f)
    return data

#Функция записи в файл
def dump(file, data):
    with open(f'{file}.pkl', 'wb') as f:
        pickle.dump(data, f)



# while True:
#     try:
#         a = load('za_last_price_rsi')
#         #l = []
#         max_key = max(a, key=lambda x: a[x])
#         max_value = a[max_key]
#         print(max_key, max_value)
#         # for i in a:
#         #     l.append(a[i])
        
#         # print(max(l))
#             #if a[i] > 51:


#             #print(i, a[i])

#         #print(a['BTCUSDT'])

#     except Exception as e:
#         print(e)
#         continue
        


#     time.sleep(5)



#Посмотреть данные по списку\
a = 1111
while True:

    time.sleep(5)

    file2 = open(f"za_last_price_5.pkl", "rb")
    last_price_5 = pickle.load(file2)
    #print(len(last_price_5['']))
    file2.close()

    file3 = open(f"za_last_price_sma.pkl", "rb")
    last_price_sma = pickle.load(file3)
    print(last_price_sma['BTCUSDT'][-1])
    file3.close()




#Посмотреть максимум и минимум выгруженного списка
while True:
    try:
        a = load('za_last_price_rsi')
        #print(a['SNTUSDT'])
        l = []
        max_key = max(a, key=lambda x: a[x])
        max_value = a[max_key]

        min_key = min(a, key=lambda x: a[x])
        min_value = a[min_key]

        print()
        print(max_key, max_value)
        print(min_key, min_value)
        print()

        # # for i in a:
        # #     l.append(a[i])
        
        # # print(max(l))
        #     #if a[i] > 51:


        #     #print(i, a[i])

        # #print(a['BTCUSDT'])

    except Exception as e:
        print(e)
        continue
        


    time.sleep(5)
