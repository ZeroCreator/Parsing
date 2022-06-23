# При помощи методов select() и select_one() для нахождения
# запрашиваемых элементов можно использовать некоторые CSS селекторы.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.select("li:nth-of-type(3)"))

# В данном примере используется CSS селектор, который выводит на экран HTML-код третьего по счету элемента li.
# [<li>Debian</li>]

# В CSS символ # используется для выбора тегов по их id-атрибутам.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.select_one("#mylist"))

# В данном примере выводятся элементы, которых есть id под названием mylist.
# <ul id="mylist" style="width:150px">
# <li>Solaris</li>
# <li>FreeBSD</li>
# <li>Debian</li>
# <li>NetBSD</li>
# <li>Windows</li>
# </ul>

