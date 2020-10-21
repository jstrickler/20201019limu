import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

# print(doc)
# root = doc.getroot()
# print(root)
# print(root.tag)

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")
print('-' * 60)

doc = ET.parse('knights.xml')

for knight in doc.findall('.//knight'):
    name = knight.findtext('name')
    print(f"{knight.get('title')} {name}")
