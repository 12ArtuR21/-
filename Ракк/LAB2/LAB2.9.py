import paho.mqtt.client as mqtt
import requests
import json
import time
URL = "https://api.worldbank.org/v2/country/bra;arg/indicator/NY.GDP.MKTP.CD?format=json&date=2010:2020"
TOPIC_BRA = "gdp/brazil"
TOPIC_ARG = "gdp/argentina"
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    country = "Бразилия" if msg.topic == TOPIC_BRA else "Аргентина"
    print(f"\nВВП {country} (2010-2020)")
    for item in data:
        val = item['value']
        if val is None: print(f"{item['date']}: нет данных")
        else: print(f"{item['date']}: {round(val / 1e9, 2)} млрд $")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe(TOPIC_BRA)
sub.subscribe(TOPIC_ARG)
sub.loop_start()
response = requests.get(URL, timeout=10)
raw_data = response.json()
data = raw_data[1]
bra_data = [item for item in data if item["countryiso3code"] == "BRA"]
arg_data = [item for item in data if item["countryiso3code"] == "ARG"]
pub = mqtt.Client()
pub.connect("broker.hivemq.com", 1883, 60)
pub.loop_start()
pub.publish(TOPIC_BRA, json.dumps(bra_data))
pub.publish(TOPIC_ARG, json.dumps(arg_data))
time.sleep(5)
pub.loop_stop()
pub.disconnect()
sub.loop_stop()
sub.disconnect()