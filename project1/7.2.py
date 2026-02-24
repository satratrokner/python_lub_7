import requests
import os

API_KEY = os.environ.get('NEWSAPI_API_KEY')

if not API_KEY:
    print("Ошибка: API ключ не найден в переменных окружения!")
    print("Установите переменную NEWSAPI_API_KEY")
    exit()

query = input("Введите тему новостей (например: technology, sport, business): ")

url = f"https://newsapi.org/v2/everything?q={query}&language=ru&pageSize=5&apiKey={API_KEY}"

try:

    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        print("Ошибка:", data)
        exit()

    articles = data["articles"]

    for i, article in enumerate(articles, start=1):
        print(f"Новость {i}")
        print(f"Источник: {article['source']['name']}")
        print(f"Автор: {article['author']}")
        print(f"Заголовок: {article['title']}")
        print(f"Описание: {article['description']}")
        print(f"Дата публикации: {article['publishedAt']}")
        print(f"Ссылка: {article['url']}")
except RequestException:
    print("Ошибка: Проблема с подключением к интернету")
except ValueError:
    print("Ошибка: Неверный формат ответа от сервера")
except KeyError as e:
    print(f"Ошибка: Отсутствует поле {e} в ответе API")