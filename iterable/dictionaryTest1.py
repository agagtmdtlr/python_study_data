# 사전 = {키1:값1, 키2:값2, ... , 키n:갑n}
# '키'는 문자열이어야 하고, unique이어야 합니다.
# '값'은 any type이든 가능합니다.
# 순서를 따지지 않고,'키'는 중복될 수 없습니다.

mydict = {'name':'pey',
          'phone':'01011112222',
          'birth':'1225'}

# 해당 키에 대한 값을 쓰기 합니다.
# 만약 해당 키가 이미 존재한다면 OverWrite가 됩니당
mydict['name'] = '홍길동'
mydict['address'] = '용산구 도원동'

# print('\n'.join(mydict.values()))
#
# #존재하는 key를 이용하여 value를 출력합니다.
# print(mydict['birth'])
#
# #존재하지 않는 key는 keyError가 발생합니다.
# # print(mydict['age'])
#
# #get('찾을키',디폴트_값)
# print((mydict.get('age',10)))
#
# if 'address' in mydict :
#     print('있슴')
# else :
#     print('업슴')

# del mydict['phone']
# print(mydict.get('phone'))
# mydict.clear()
print(mydict['phone'])
