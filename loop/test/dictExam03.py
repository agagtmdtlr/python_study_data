members = {
              'hong' : {'name':'홍길동',
                        'age':10,
                        'address':'경기'},
              'shin': {'name':'신사임당',
                       'age':20,
                       'address':'서울'},
              'lee'  : {'name':'이순신',
                        'age': 30,
                        'address':'제주'},
              'kim'  : {'age': 40,
                        'address':'울릉도',
                        'name':'김유신'}
            }
for i1,i2 in members.items():
    print(i1,i2)

members['lee']['age'] = 50
print(members['lee']['age'])
members.update(['lee']['age'])

