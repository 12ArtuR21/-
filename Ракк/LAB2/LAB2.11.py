import paho.mqtt.client as mqtt
import random
import time
even_nums = []
odd_nums = []
def on_message(client, userdata, msg):
    if msg.topic == "sensor/avg":
        print(f"Среднее значение: {msg.payload.decode()}")
        return
    val = float(msg.payload.decode())
    if msg.topic == "sensor/even": even_nums.append(val)
    elif msg.topic == "sensor/odd": odd_nums.append(val)
    all_nums = even_nums + odd_nums
    if all_nums:
        avg = sum(all_nums) / len(all_nums)
        client.publish("sensor/avg", str(round(avg, 2)))
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe("sensor/even")
sub.subscribe("sensor/odd")
sub.subscribe("sensor/avg")
sub.loop_start()
pub = mqtt.Client()
pub.connect("broker.hivemq.com", 1883, 60)
pub.loop_start()
while True:
    num = random.randint(1, 100)
    topic = "sensor/even" if num % 2 == 0 else "sensor/odd"
    pub.publish(topic, str(num))
    print(f"Отправлено {num} в {topic}")
    time.sleep(1)
pub.loop_stop()
pub.disconnect()
sub.loop_stop()
sub.disconnect()