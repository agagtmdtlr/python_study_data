import json

filename = 'data/some.json'
# unexpected utf-8 BOM (decode using utf-8-sig)
myfile = open(filename,'rt',encoding='utf-8-sig') # encoding='utf-8-sig'
mystring = myfile.read()
jsondata = json.loads(mystring)
print(type(jsondata))
print(jsondata)
# 사람 정보 출력
name = jsondata['member']['name']
address = jsondata['member']['address']
phone = jsondata['member']['phone']

print('이름 : ' + name)
print('주소 : ' + address)
print('전화 번호 : ' + phone)

#웹 페이지 정보 출력
cafename = jsondata['web']['cafename']
id = jsondata['web']['id']

print('cafename : '+ cafename)
print('아이디 : '+ id)
