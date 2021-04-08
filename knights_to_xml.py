import lxml.etree as et
# import xml.etree.ElementTree as et

root = et.Element('knights')
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        # def SubElement(parent, tag, **attrs): ...
        knight = et.SubElement(root, 'knight', title=title)
        k_name = et.SubElement(knight, 'name')
        k_name.text = name
        et.SubElement(knight, 'color').text = color
        et.SubElement(knight, 'quest').text = quest
        et.SubElement(knight, 'comment').text = comment

raw_xml = et.tostring(root, pretty_print=True,
                      encoding='utf-8', xml_declaration=True)
xml = raw_xml.decode()
print(xml)

doc = et.ElementTree(root)  # create an ElementTree object
doc.write('knights.xml', pretty_print=True, xml_declaration=True,
          encoding='utf-8')
