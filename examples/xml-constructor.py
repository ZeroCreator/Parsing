from xml.etree import ElementTree

root = ElementTree.Element("student")

first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"

second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"

scores = ElementTree.SubElement(root, "scores")

modul1 = ElementTree.SubElement(scores, "modul1")
modul1.text = "100"

modul2 = ElementTree.SubElement(scores, "modul2")
modul2.text = "80"

modul3 = ElementTree.SubElement(scores, "modul3")
modul3.text = "90"

tree = ElementTree.ElementTree(root)
tree.write("student.xml")
