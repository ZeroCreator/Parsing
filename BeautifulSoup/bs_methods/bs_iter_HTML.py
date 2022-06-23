# Метод recursiveChildGenerator() позволяет
# перебрать содержимое HTML-документа.


from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    for child in soup.recursiveChildGenerator():

        if child.name:
            print(child.name)


# html
# head
# title
# meta
# body
# h2
# ul
# li
# li
# li
# li
# li
# p
# p