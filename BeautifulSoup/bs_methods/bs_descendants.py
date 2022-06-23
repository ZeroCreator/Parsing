# При помощи атрибута descendants можно получить список всех
# потомков (дочерних элементов всех уровней) рассматриваемого тега.
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    root = soup.body

    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)

# ['h2', 'ul', 'li', 'li', 'li', 'li', 'li', 'p', 'p']
