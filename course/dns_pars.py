import requests

"Получаем перечень карточек с информацией по видеокартам"

def get_content(url):
    """функция получает текст с url и сохраняет его в файл"""
    header = {"User-Agent":
                  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
              "Accept": "image/avif,image/webp,*/*"
              }
    response = requests.get(url, headers=header)
    with open('dns.html', 'w') as f:
        f.write(response.text)

def parse_content():
    """функция возвращает url, который надо парсить"""
    url = 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'
    get_content(url)


if __name__ == "__main__":
    parse_content()