from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree


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

human = Element("Person",attrib={'id':'kim'})
name = SubElement(human,'name')
name.text = '김철수'
age = SubElement(human,'age')
age.text = '30'
address =SubElement(human,'address')
address.text = '용산구 도원동'
indent(human)

xmlFile = 'xmlTest.xml'

ElementTree(human).write(xmlFile, encoding='utf-8')

print(xmlFile + '파일이 생성되었습니다.')
print('작업 완료')