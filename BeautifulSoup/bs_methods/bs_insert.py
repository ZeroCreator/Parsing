# Метод insert() позволяет вставить тег в определенно выбранное место.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    newtag = soup.new_tag('li')
    newtag.string = 'OpenBSD'

    ultag = soup.ul

    ultag.insert(2, newtag)

    print(ultag.prettify())

# В примере показано, как поставить тег li на третью позицию в выбранном ul теге.
# <ul id="mylist" style="width:150px">
#  <li>
#   Solaris
#  </li>
#  <li>
#   OpenBSD
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
# </ul>