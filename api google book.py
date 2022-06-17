import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
query = "Моби Дик"

params = {"q": query, "maxResults": 3}
response = requests.get(endpoint, params=params).json()
for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume["title"]
    published = volume.get("publishedDate", "год издания неизвестен")
    description = volume.get("description", "описание отсутствует")
    print(f"{title} ({published}) | {description}")



