import requests

API_KEY = "fbeca65cf99cc7dfbb7889bd40af93bd"

city = input("Введите название города: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

response = requests.get(url)
data = response.json()

if response.status_code != 200:
    print("Ошибка:", data.get("message"))
    exit()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
weather_description = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]
city_name = data["name"]
country = data["sys"]["country"]

print(f"Город: {city_name}, {country}")
print(f"Температура: {temperature} °C")
print(f"Ощущается как: {feels_like} °C")
print(f"Состояние: {weather_description}")
print(f"Влажность: {humidity} %")
print(f"Давление: {pressure} hPa")
print(f"Скорость ветра: {wind_speed} м/с")