# mydict = {'김철수':35,'박영희':50,'홍길동':40}
#
# print('key :',mydict.keys())
# print('value : ',mydict.values())
# for (ky,val) in mydict.items():
#     print(f'{ky}의 나이는 {val}살입니다.')
#
#
# # in 키워드
# findkey = '배철수'
# if findkey in mydict :
#     print('존재')
# else :
#     print('미존재')
#
# print(mydict.items())
# #dict.pop( key ) : value 지우기
# result = mydict.pop('홍길동')
# print(result)
# print(mydict)

newdict = dict()
print(newdict)
newdict['a'] = ['가',100]
newdict['b'] = ['나',200]
print(newdict)
print(id(newdict))

