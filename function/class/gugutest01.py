def gugu(n):
    return [n*i for i in range(1,10)]

def gugu2(n1,n2):
    #logic1
    result = []
    # for i in range(n1,n2+1):
    #     result.append([i*x for x in range(1,10)])
    #logic2
    imsilist = [ x*y for x in range(n1,n2+1) for y in range(1,10)]
    imsilen = len(list(range(n1,n2+1)))
    result =[ imsilist[9*i:9*(i+1)] # 0-8 9-17 18-26
              for i in range(imsilen) ]
    return result

print(gugu(2))
print(gugu2(2,4))

list1 = [1,2,3,4,5]
list2 = [6,7,8]
list3 = [i for i in zip(list1,list2)]
print(list3)