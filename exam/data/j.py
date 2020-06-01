import json

filename = 'some3.json'

myfile = open(filename, 'rt', encoding='utf-8-sig')
mystring = myfile.read()
jsondata = json.loads(mystring)

print('이름 : ' +  jsondata['member']['name'] )
print('주소 : ' +  jsondata['member']['address']  )
print('나이 : ' +  jsondata['member']['age']  )

print('직위 : ' + jsondata['company']['jik'] )
print('사번 : ' + jsondata['company']['sabun']   )
print('finished')