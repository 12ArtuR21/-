import paho.mqtt.client as mqtt
import base64
import time
TOPIC = "files/image"
def on_message(client, userdata, msg):
    encoded_data = msg.payload.decode('ascii')
    file_data = base64.b64decode(encoded_data)
    with open("new_image.png", "wb") as f: f.write(file_data)
    print(f"Файл получен и сохранен как new_image.png ({len(file_data)} байт)")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe(TOPIC)
sub.loop_start()
with open("image.png", "rb") as f: file_data = f.read()
encoded_data = base64.b64encode(file_data).decode('ascii')
print(f"Файл image.png закодирован. Длина строки: {len(encoded_data)}")
pub = mqtt.Client()
pub.connect("broker.hivemq.com", 1883, 60)
pub.loop_start()
pub.publish(TOPIC, encoded_data)
time.sleep(3)
pub.loop_stop()
pub.disconnect()
sub.loop_stop()
sub.disconnect()