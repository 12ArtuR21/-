import paho.mqtt.client as mqtt
def pub_message(client, userdata, msg):
    print("Publisher получил:", msg.payload.decode())
pub = mqtt.Client()
pub.on_message = pub_message
pub.connect("broker.hivemq.com", 1883, 60)
pub.subscribe("echo/out")
pub.loop_start()
def sub_message(client, userdata, msg):
    client.publish("echo/out", "ECHO: " + msg.payload.decode())
sub = mqtt.Client()
sub.on_message = sub_message
sub.connect("broker.hivemq.com", 1883, 60)
sub.subscribe("echo/in")
sub.loop_start()
while True:
    text = input()
    pub.publish("echo/in", text)