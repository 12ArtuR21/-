import paho.mqtt.client as mqtt
import re
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_DIGITS = "test/python/digits"
TOPIC_SYMBOLS = "test/python/symbols"
def main():
    user_input = input("Строка: ")
    digits = "".join(re.findall(r'\d', user_input))
    symbols = "".join(re.findall(r'\D', user_input))
    print(f"Отправление цифр: '{digits}' в топик {TOPIC_DIGITS}")
    print(f"Отправление символов: '{symbols}' в топик {TOPIC_SYMBOLS}")
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    try:
        client.connect(BROKER, PORT, 60)
        client.publish(TOPIC_DIGITS, digits)
        client.publish(TOPIC_SYMBOLS, symbols)
        client.loop(timeout=1.0)
        print("Сообщения успешно отправлены!")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    finally:
        client.disconnect()
if __name__ == "__main__":
    main()