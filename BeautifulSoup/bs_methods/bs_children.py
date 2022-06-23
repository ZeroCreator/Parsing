# При помощи атрибута children можно вывести все дочерние теги.

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    root = soup.html

    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)

# ['head', 'body'] - у тегов html есть два дочерних элемента: head и body.


