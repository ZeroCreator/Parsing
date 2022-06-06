import requests

res = requests.get("http://docs.python.org/3.10/")
print(res.status_code)
print(res.headers['Content-Type'])

#print(res.content)
#print(res.text)

with open("python.png", "wb") as f:
    f.write(res.content)


res1 = requests.get("http://yandex.ru/search/",
                   params={"text": "Stepic",
                            "test": "test1",
                           "name":"Name With Spase",
                           "list": ["test1", "test2"]
                    })
print(res1.status_code)
print(res1.headers['Content-Type'])
print(res1.url)
#print(res1.text)



