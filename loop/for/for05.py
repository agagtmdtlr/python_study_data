list1 = list('life is either a daring adventure or nothing'.split(' '))
for i in range(len(list1)):
    if i%2==0:
       list1[i] = list1[i].upper()

print('#'.join(list1))