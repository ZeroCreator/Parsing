from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print("HTML: {0}, name: {1}, text: {2}".format(soup.h2,
                                                   soup.h2.name, soup.h2.text))


# HTML: <h2>Operating systems</h2>, name: h2, text: Operating systems