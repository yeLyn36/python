import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element('Drink')
name = SubElement(root, 'name')
price = SubElement(root, 'price')
ice = SubElement(root, "ice")
sugar = SubElement(root, "sugar")
pearl = SubElement(root, "pearl")
name.text = "아이스아메리카노"
price.text = "2800원"
ice.text = "50%"
sugar.text = "50%"
pearl.text = "없음"

# rootOpen = "<Drink>"
# rootClose = "</Drink>"
# name = ("<name>" + name + "</name>")
# price = ("<price>" + price + "</price>")
# ice = ("<ice>" + ice + "</ice>")
# sugar = ("<sugar>" + sugar + "</sugar>")
# pearl = ("<pearl>" + pearl + "</pearl>")

ET.ElementTree(root).write('Drink.xml', encoding='utf8', xml_declaration=True)