import lxml.etree as et

doc = et.parse('knights.xml')

print(doc)
root = doc.getroot()
print(root, root.tag, root.text)
for k in root.findall('knight'):
    name = k.findtext('name')
    color = k.findtext('color')
    print(name, color)
print("-" * 60)

solar_doc = et.parse('DATA/solar.xml')

mars = solar_doc.find('''.//planet[@planetname="Mars"]''')
print(mars)
for moon in mars.findall('moon'):
    print(moon.text)
print()

for planet in solar_doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")

