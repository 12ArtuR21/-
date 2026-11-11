import paho.mqtt.client as mqtt
import random, time
P = "nuriev_lab5/"  # Чтобы не ловить чужие сообщения
def on_message(client, userdata, msg):
    print(f"{msg.topic} = {msg.payload.decode()}")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe(P + "home/living_room/+")
sub.subscribe(P + "home/+/temperature")
sub.subscribe(P + "home/#")
sub.loop_start()
pub = mqtt.Client()
pub.connect("broker.hivemq.com", 1883, 60)
pub.loop_start()
while True:
    pub.publish(P + "home/living_room/temperature", f"{random.randint(18,25)}C")
    pub.publish(P + "home/living_room/humidity", f"{random.randint(30,70)}%")
    pub.publish(P + "home/kitchen/temperature", f"{random.randint(20,30)}C")
    pub.publish(P + "home/garage/door_status", random.choice(["open","closed"]))
    time.sleep(3)