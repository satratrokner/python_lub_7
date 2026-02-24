import requests

API_KEY = "921566c517414b3b8b1b34ebbd123a33"

# ввод темы
query = input("Введите тему новостей (например: technology, sport, business): ")

# формируем URL
url = f"https://newsapi.org/v2/everything?q={query}&language=ru&pageSize=5&apiKey={API_KEY}"

# отправляем запрос
response = requests.get(url)
data = response.json()

# проверка
if data["status"] != "ok":
    print("❌ Ошибка:", data)
    exit()

articles = data["articles"]

# вывод
print("\n===== Найденные новости =====\n")

for i, article in enumerate(articles, start=1):
    print(f"🔹 Новость {i}")
    print(f"Источник: {article['source']['name']}")
    print(f"Автор: {article['author']}")
    print(f"Заголовок: {article['title']}")
    print(f"Описание: {article['description']}")
    print(f"Дата публикации: {article['publishedAt']}")
    print(f"Ссылка: {article['url']}")
    print("-" * 40)