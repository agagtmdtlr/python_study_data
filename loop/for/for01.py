total = 0
# for 단수(tuple,var...) in 복수(list,tuple,range,enumerate...):
for i in range(1,11):
    total += i
print('1부터 10까지 총합은 %d입니다' %(total))

#1,4,7,10,...100 = 1717
total=0
for i in range(1,101,3):
    total+=i
print('1,4,7,10,...100 = %d' %(total))
#97+92+87+..+7+2 = 990
total=0
for i in range(97,1,-5):
    total+=i
print('97+92+87+..+7+2 = %d' %(total))
#1*1+6*6+11*11+...+96*96=63670
total=0
for i in range(1,97,5):
    total+=pow(i,2)
print('1*1+6*6+11*11+...+96*96 = %d' %(total))