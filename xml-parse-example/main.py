from lxml import etree


with open('data.xml', encoding='utf8') as file:
    xml = etree.parse(file)

with open('out.xml', 'wb') as file:
    xml.write(file, pretty_print=True, encoding='utf-8', xml_declaration=True)


# import code; code.interact(local=dict(globals(), **locals()))
