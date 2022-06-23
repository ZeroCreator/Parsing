# Метод replace_with() заменяет содержимое выбранного элемента.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    tag = soup.find(text="Windows")
    tag.replace_with("OpenBSD")

    print(soup.ul.prettify())

# В примере показано, как при помощи метода find() найти определенный элемент, а затем,
# используя метод replace_with(), заменить его содержимое.
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
#   OpenBSD
#  </li>
# </ul>