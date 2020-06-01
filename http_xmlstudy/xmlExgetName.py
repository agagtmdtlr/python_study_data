from xml.etree.ElementTree import parse

xmlfile = 'concat_data/xmlExgetName.xml'
# parse : xml 문서가 제대로 작성이 되었는지를 분석하는 동작
tree = parse(xmlfile)
root = tree.getroot()
print(type(root)) # if not return None : get success(element)

families = root.findall('가족')
print(len(families))
###########################
print(root.keys())
print('-'*30)

print(root.items())
print('-'*30)

print(root.get('설명'))
print('-'*30)

print(root.get('qwert','없으면 기본값'))
print('-'*30)
############################
family = root.find('가족') # 하나의 element 찾기
print(family)
############
for onefamily in families:
    members = onefamily.getchildren()
    # print(len(members))
    for onesaram in members:
        if len(onesaram) >= 1:
            print(onesaram[0].text)
        else :
            print(onesaram.attrib['이름'])
    print('-'*40)
    #end for
#end for


print('finished')