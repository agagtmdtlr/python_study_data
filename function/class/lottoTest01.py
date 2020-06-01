import random
#금주 로또 번호 : 5,10,15,20,25,30
#2등 로또 번호 : 40
b = True
set1 = set()
count = 0
while b :
    count += 1
    temp = random.randint(1,45)
    set1.add(temp)
    if len(set1) == 6 :
        print('금주 로또 번호 :',','.join(map(str,sorted(set1))))
    if len(set1) == 7 :
        print('2등 로도 번호 :',temp)
        break

print(count)
