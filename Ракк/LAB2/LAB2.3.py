import paho.mqtt.client as mqtt
import psutil
import json
import time
import warnings
warnings.filterwarnings("ignore")
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"CPU: {data['cpu_percent']}% | RAM: {data['memory_percent']}% | Disk: {data['disk_percent']}%")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe("system/monitor")
sub.loop_start()
pub = mqtt.Client()
pub.connect("broker.hivemq.com", 1883, 60)
pub.loop_start()
while True:
    data = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }
    pub.publish("system/monitor", json.dumps(data))
    time.sleep(4)