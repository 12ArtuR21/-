import paho.mqtt.client as mqtt
import random
import time
def on_message(client, userdata, msg):
    if msg.topic == "sensors/temp":
        temp = float(msg.payload.decode())
        print(f"Температура: {temp}°C")
        if temp > 80:
            client.publish("alerts/temp", "ALERT: High temperature!")
    else:print(f"{msg.payload.decode()}")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe("sensors/temp")
sub.subscribe("alerts/temp")
sub.loop_start()
sensor = mqtt.Client()
sensor.connect("broker.hivemq.com", 1883, 60)
sensor.loop_start()
while True:
    sensor.publish("sensors/temp", str(random.randint(0, 100)))
    time.sleep(3)