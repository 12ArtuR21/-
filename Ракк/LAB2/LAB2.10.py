import paho.mqtt.client as mqtt
import requests
import time
def on_message(client, userdata, msg):
    parts = msg.topic.split("/")
    print(f"ID: {parts[-2]} | {parts[-1]}: {msg.payload.decode()}")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe("user/#")
sub.loop_start()
data = requests.get("https://reqres.in/api/users/").json()
pub = mqtt.Client()
pub.connect("broker.hivemq.com", 1883, 60)
pub.loop_start()
for u in data["data"]:
    pub.publish("user/" + str(u["id"]) + "/email", u["email"])
    pub.publish("user/" + str(u["id"]) + "/avatar", u["avatar"])
time.sleep(5)
pub.loop_stop()
pub.disconnect()
sub.loop_stop()
sub.disconnect()