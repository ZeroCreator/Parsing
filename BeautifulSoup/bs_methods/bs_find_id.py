# При помощи метода find() можно найти элементы страницы,
# используя различные опорные параметры, id в том числе.

from bs4 import BeautifulSoup


# Код в примере находит тег ul, у которого id mylist.
# Строка в комментарии является альтернативным способом
# выполнить то же самое задание.
with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    # print(soup.find("ul", attrs={ "id" : "mylist"}))
    print(soup.find("ul", id="mylist"))


# <ul id="mylist" style="width:150px">
# <li>Solaris</li>
# <li>FreeBSD</li>
# <li>Debian</li>
# <li>NetBSD</li>
# <li>Windows</li>
# </ul>