from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree

mydict = {'kim': ('김철수',30,'남자','마포 공독동'),'park':('박영희',40,'여자','용산 도원동')}
members = Element('members')

for key,mytuple in mydict.items():
    myattrib = {'aaa':'bbb','ccc':'ddd'}
    mem = SubElement(members,'member',attrib=myattrib) #<members><member></member></members>
    mem.attrib['id'] = key
    SubElement(mem,'name').text = mytuple[0]
    SubElement(mem, 'age').text = str(mytuple[1])
    SubElement(mem, 'gender').text = mytuple[2]
    SubElement(mem, 'address').text = mytuple[3]

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

indent(members)

xmlfile = 'concat_data/xmlEx_03.xml'

ElementTree(members).write(xmlfile,encoding='utf-8')
print(xmlfile+'파일 저장됨')