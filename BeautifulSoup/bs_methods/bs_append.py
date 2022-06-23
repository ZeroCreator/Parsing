# Метод append() добавляет в рассматриваемый HTML-документ новый тег.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    # Для начала, требуется создать новый тег при помощи метода new_tag().
    newtag = soup.new_tag('li')
    newtag.string = 'OpenBSD'

    # Далее создается сноска на тег ul.
    ultag = soup.ul

    # Затем созданный ранее тег li добавляется к тегу ul.
    ultag.append(newtag)

    # Таким образом, тег ul выводится аккуратно отформатированным.
    print(ultag.prettify())

# <ul id="mylist" style="width:150px">
#  <li>
#   Solaris
#  </li>
#  <li>
#   FreeBSD
#  </li>
#  <li>
#   Debian
#  </li>
#  <li>
#   NetBSD
#  </li>
#  <li>
#   Windows
#  </li>
#  <li>
#   OpenBSD
#  </li>
# </ul>