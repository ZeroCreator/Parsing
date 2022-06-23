import requests_test

# response = requests.get("http://docs.python.org/3.5/")
# атрибуты, доступных для объектов ответа.
# print(response.status_code)
# print(response.reason)
# print(response.url)
# print(response.headers['Content-Type'])
#
# headers = {"X-Request-Id": "<my-request-id>"}
# response = requests.get("https://example.org", headers=headers)
# print(response.request.headers)
# print(response.headers['Content-Type'])

# response = requests.get("https://api.thedogapi.com/v1/breeds/1")
# print(response.headers.get("Content-Type"))
# print(response.json())
# print(response.json()["name"])


# атрибуты, доступных для объектов запроса
# request = response.request
# print(request.url)
# print(request.method)
# print(request.path_url)
# print(request.headers)
# print(response.headers)

#print(res.content)
# print(res.text)
#
# with open("python.html", "w") as f:
#     f.write(res.text)


#res1 = requests.get("http://yandex.ru/search/",
#                    params={"text": "Stepic",
#                             "test": "test1",
#                            "name":"Name With Spase",
#                            "list": ["test1", "test2"]
#                     })
# print(res1.status_code)
# print(res1.headers['Content-Type'])
# print(res1.url)
#print(res1.text)



# query_params = {"gender": "female", "nat": "de"}
# response = requests.get("https://randomuser.me/api/", params=query_params).json()
# print(response)

# Ключи API
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Замените DEMO_KEY ниже своим собственным ключом, если вы его сгенерировали.
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
print(response)
print(response.json()) # используем .json() для преобразования ответа в словарь Python
photos = response.json()["photos"] # извлекаем поле photos
print(f"Найдено {len(photos)} фотографий.")
print(photos[7]["img_src"]) # получаем URL-адрес изображения для одной из фотографий