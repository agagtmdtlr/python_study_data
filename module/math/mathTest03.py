import math

def softmax(mylist):
    newlist = [math.exp(x) for x in mylist]
    total = sum(newlist)
    mylist = [x/total for x in newlist]
    return mylist

mylist = [0.1,1.0,2.0]
result = softmax(mylist)
print(result)
