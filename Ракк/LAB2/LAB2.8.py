import paho.mqtt.client as mqtt
import requests
import json
import time
API_KEY = "9b9ab99e13a0bc2ab9522d6d1688e95c"
URL = "https://api.openweathermap.org/data/2.5/forecast"
TOPIC_CURRENT, TOPIC_DAILY = "weather/current", "weather/daily"
params = {"lat": 51.46, "lon": 55.09, "appid": API_KEY, "units": "metric", "lang": "ru"}
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    if msg.topic == TOPIC_CURRENT:
        print(f"Текущая погода в Оренбурге")
        print(f"Температура: {data['main']['temp']}°C")
        print(f"Ощущается: {data['main']['feels_like']}°C")
        print(f"Погода: {data['weather'][0]['description']}")
    elif msg.topic == TOPIC_DAILY:
        print(f"Прогноз:")
        for item in data[:5]: print(f"{item['dt_txt']}: {item['main']['temp']}°C, {item['weather'][0]['description']}")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe(TOPIC_CURRENT)
sub.subscribe(TOPIC_DAILY)
sub.loop_start()
response = requests.get(URL, params=params, timeout=15)
data = response.json()
if response.status_code != 200: print(f"Ошибка API: {data}")
else:
    pub = mqtt.Client()
    pub.connect("broker.hivemq.com", 1883, 60)
    pub.loop_start()
    pub.publish(TOPIC_CURRENT, json.dumps(data["list"][0]))
    pub.publish(TOPIC_DAILY, json.dumps(data["list"]))
    time.sleep(6)
    pub.loop_stop()
    pub.disconnect()
    sub.loop_stop()
    sub.disconnect()