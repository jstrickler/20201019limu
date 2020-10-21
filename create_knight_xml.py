import lxml.etree as ET
from pprint import pprint

knight_info = []
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        knight_info.append(fields)

pprint(knight_info)
print()


root_element = ET.Element('knights')
for name, title, color, quest, comment in knight_info:
    knight = ET.SubElement(root_element, 'knight', title=title)
    ET.SubElement(knight, 'name').text = name
    ET.SubElement(knight, 'color').text = color
    ET.SubElement(knight, 'quest').text = quest
    ET.SubElement(knight, 'comment').text = comment


print(ET.tostring(root_element, xml_declaration=True, pretty_print=True).decode())

tree = ET.ElementTree(root_element)

tree.write('knights.xml', pretty_print=True, xml_declaration=True)
