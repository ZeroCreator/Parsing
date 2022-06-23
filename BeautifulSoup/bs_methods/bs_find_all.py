# При помощи метода find_all() можно найти все элементы, которые соответствуют заданным критериям.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))


# li: Solaris
# li: FreeBSD
# li: Debian
# li: NetBSD
# li: Windows

    # В данном примере показано, как найти все h2 и p элементы, после чего вывести их содержимое на экран.
    tags = soup.find_all(['h2', 'p'])

    for tag in tags:
        print(" ".join(tag.text.split()))


# Метод find_all() также может использовать функцию, которая определяет, какие элементы должны быть выведены.


def myfun(tag):
    return tag.is_empty_element


with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    tags = soup.find_all(myfun)
    print(tags)

# [<meta charset="utf-8"/>]

# Также можно найти запрашиваемые элементы, используя регулярные выражения.
import re

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    strings = soup.find_all(string=re.compile('BSD'))

    for txt in strings:
        print(" ".join(txt.split()))


# FreeBSD
# NetBSD
# FreeBSD is an advanced computer operating system used to power modern servers, desktops, and embedded platforms.