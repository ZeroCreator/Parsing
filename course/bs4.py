import requests
import bs4 as bs


# Получить страничку поста
url = 'https://www.franksonnenbergonline.com/blog/are-you-grateful/'
response = requests.get(url)
response.raise_for_status()
print(response.text)

# Парсинг поста
soup = bs(response.text, 'lxml')
print(soup.prettify())
