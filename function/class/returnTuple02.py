def myfunc2(list1):
    for i in range(len(list1)):
        list1[i] = abs(list1[i])
    list1 = sorted(list1)
    total = sum(list1)
    return  (list1[-1],list1[0],total,total//len(list1))

list1 = [10,-20,30,-50,40]
print(myfunc2(list1))
print([abs(i) for i in list1])
list1 = [10,-20,30,-50,40]
list2 = [abs(i) for i in list1 if i < 0]
print(list2)