import websocket
import pickle
import json
import datetime
import pandas as pd

asset = 'BTCUSDT'  # Символ актива
duration = 60  # Длительность сохранения цен (в секундах)
end_time = datetime.datetime.now() + datetime.timedelta(seconds=duration)

# Создание пустого DataFrame для хранения цен
prices = pd.DataFrame(columns=['time', 'price'])

def on_message(ws, message):
    file = open(f"za_last_price.pkl", "rb+")

    data = json.loads(message)
    xuui = pickle.load(file)

    for item in data:
        if item['s'].endswith('USDT'):
            xuui[item['s']] = float(item['c'])
    

    file.seek(0)
    pickle.dump(xuui, file)

    file.close() # Закрыть файл


if __name__ == "__main__":
    #ws = websocket.WebSocketApp("wss://stream.binance.com:9443/stream?streams=ltcbtc@aggTrade/ethbtc@aggTrade",
    ws = websocket.WebSocketApp("wss://fstream.binance.com/ws/!ticker@arr",
                              on_message = on_message)
    ws.run_forever()

