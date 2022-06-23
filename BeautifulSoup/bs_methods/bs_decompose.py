# Метод decompose() удаляет определенный тег из структуры документа и уничтожает его.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    ptag2 = soup.select_one("p:nth-of-type(2)")

    ptag2.decompose()

    print(soup.body.prettify())

# В данном примере показано, как удалить второй элемент p в документе.
# <body>
#  <h2>
#   Operating systems
#  </h2>
#  <ul id="mylist" style="width:150px">
#   <li>
#    Solaris
#   </li>
#   <li>
#    FreeBSD
#   </li>
#   <li>
#    Debian
#   </li>
#   <li>
#    NetBSD
#   </li>
#   <li>
#    Windows
#   </li>
#  </ul>
#  <p>
#   FreeBSD is an advanced computer operating system used to
#           power modern servers, desktops, and embedded platforms.
#  </p>
# </body>