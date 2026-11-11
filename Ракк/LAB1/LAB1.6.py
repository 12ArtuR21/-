import requests

API_KEY = "reqres_3ec2ce07be55457aa8a410a28d6e3758"
BASE_URL = "https://reqres.in/api/users"
print("ВЫПОЛНЕНИЕ POST ЗАПРОСА")
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
group = input("Введите номер учебной группы: ")
phone = input("Введите марку вашего телефона: ")
car = input("Введите желаемую марку автомобиля: ")
post_payload = {
    "name": name,
    "surname": surname,
    "group": group,
    "phone": phone,
    "car": car
}
post_response = requests.post(BASE_URL, json=post_payload)
print(f"Статус-код ответа: {post_response.status_code}")
print("Ответ сервера (текст):")
print(post_response.text)
print("\nВЫПОЛНЕНИЕ PUT-ЗАПРОСА")
new_car = input("Введите новую желаемую марку автомобиля: ")
put_payload = { "car": new_car }
put_response = requests.put(f"{BASE_URL}/{2}", json=put_payload)
print(f"Статус-код ответа: {put_response.status_code}")
print("Ответ сервера:")
print(put_response.text)
print("\nВЫПОЛНЕНИЕ DELETE-ЗАПРОСА")
delete_response = requests.delete(f"{BASE_URL}/{2}")
print(f"Статус-код ответа: {delete_response.status_code}")