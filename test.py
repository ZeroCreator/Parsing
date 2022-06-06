from xml.etree import ElementTree

color_list = {
    "red": 0,
    "green": 0,
    "blue": 0
}

tree = ElementTree.fromstring("test.xml")

def foo(tree, level):


