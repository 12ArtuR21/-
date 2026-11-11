import paho.mqtt.client as mqtt
import keyboard
import time
stop = False
def on_message(client, userdata, msg):
    if msg.topic == "high": print(f"Получено в HIGH: {msg.payload.decode()}")
    elif msg.topic == "low": print(f"Получено в LOW: {msg.payload.decode()}")
sub = mqtt.Client()
sub.on_message = on_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe("high")
sub.subscribe("low")
sub.loop_start()
pub = mqtt.Client()
pub.connect("broker.hivemq.com", 1883, 60)
pub.loop_start()
def on_key(event):
    global stop
    if event.event_type != keyboard.KEY_DOWN: return
    if event.name.isdigit():
        num = int(event.name)
        if num == 0: stop = True
        elif num > 5:
            print(f" - ввод {num} - отправка в HIGH")
            pub.publish("high", event.name)
        else:
            print(f" - ввод {num} - отправка в LOW")
            pub.publish("low", event.name)
    else: print(f" - введен символ")
keyboard.hook(on_key)
while not stop: time.sleep(0.1)
keyboard.unhook_all()
sub.disconnect()
pub.disconnect()