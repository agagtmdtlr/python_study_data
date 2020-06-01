import math

def entropy(lists):
    result = []
    for i in lists:
        mydict = dict()
        for j in i:
            if j in mydict:
                mydict[j] = mydict[j]+1
            else :
                mydict[j] = 1
        sume = 0
        lens = len(i)
        for k in mydict.values():
            ek = k/lens
            sume += ek*math.log2(ek)
        result.append(abs(sume)) # 로그 지수가 1보다 작으면 해가 음수로 나온다.
        # result.append(abs(sum([k/lens*math.log2(k/lens) for k in mydict.values()])))
    return result


mylist =[['red','blue','red','blue','red'],
         ['red','blue','red','red','red'],
         ['red','red','red','red','red']]
result = entropy(mylist)
print(result)