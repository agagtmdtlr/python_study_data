def minval(*args):
    list1 = list(args)
    for i in range(1, len(list1)):
        if list1[0] > list1[i]:
            list1[0], list1[i] = list1[i], list1[0]
    print(list1[0])


minval(3, 5, 8)
minval(3, 8)
minval(8, 1, 4, 5)