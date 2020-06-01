from typing import Tuple

mylist = ['강감찬','이순신','김유신','신사임당']

for idx, value in enumerate(mylist):
    print('인덱스 : %d, 값 :  %s' %(idx,value))
print()

for aa in enumerate(mylist):
    print('인덱스 : {}, 값 :  {}'.format(aa[0],aa[1]))
print()

aa: Tuple[int, str]
for aa in enumerate(mylist):
    print('인덱스 : {}, 값 :  {}'.format(*aa))


members = {'김유신':20, '이순신':30}
for i in members:
    print(i)

for key,value in members.items():
    print('키 : {}, 값 : {}'.format(key,value))
print()

for dd in members.items():
    print('키 : {}, 값 : {}'.format(*dd))
print()

for dd in members.items():
    print('키 : {}, 값 : {}'.format(dd[0],dd[1]))
print()