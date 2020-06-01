from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree

fruit = Element('fruit') # <fruit></fruit> root element : create on memory
# subelement
SubElement(fruit,'name').text = '사과'
SubElement(fruit, 'price').text = '1000'
SubElement(fruit, 'qty').text = '10'

def indent(elem, level = 0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem) :
        if not elem.text or not elem.text.strip() :
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i

        for elem in elem :
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip() :
            elem.tail = i
    else :
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(fruit)

xmlfile = 'concat_data/xmlEx_02.xml'

ElementTree(fruit).write(xmlfile,encoding='utf-8')
print(type(fruit))
print(type(ElementTree(fruit)))
print(xmlfile+'파일 저장됨')