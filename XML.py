# В XML сами отображаем теги. Для хранения данных,
# в отличие от HTML, который для отображения данных.
# Элементы определяются с помощью тегов.
from xml.etree import ElementTree

tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

print(root[0][0].text)

for child in root:
    print(child.tag, child.attrib)

for element in root.iter("scores"): # .findall
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)

# Модификация деревьев
# Запись дерева в xml-формате (скопировали текст файла)
#tree.write("example_copy.xml")
# Добавить данные

greg = root[0]
#module1 = next(greg.iter("module1"))
#print(module1, module1.text)
#module1.text = str(float(module1.text) + 30)
#certificate = greg[2]
#certificate.set("type", "with distinction")

#tree.write("example_modified.xml")

# Добавлять или создавать элементы из другого элемента
#description = ElementTree.Element("description")
#description.text = "Showed excellent skills during the course"
#greg.append(description)

#tree.write("example_modified.xml")

# Убрать
description = greg.find("description")
greg.remove(description)

tree.write("example_modified.xml")