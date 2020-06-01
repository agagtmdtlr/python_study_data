# 1개의 정수 n을 매개 변수로 입력 받아서 1부터 nRkwldml 총합을 구하여 프린트하는 함수 mysum()을 작성해 보세요.
# 만약, 정수 n을 입력하지 않으면 기본 값으로 10을 대입하도록 합니다.
def mysum( su=10):
    total = sum([i for i in range(1,su+1)])
    print(total)

# 리스트의 요소를 비교하여 동일한 리스트인지 판단하는 함수를 작성하세요.
def equalsList( mylist1, mylist2, su=None ):
    check = True
    arr = 0

    if su is not None :
        su = abs(su)
        minlen = min(len(mylist1),len(mylist2))
        if minlen < su :
            print('비교범위 초과')
            return
        else:
            arr = su
    else:
        if len(mylist1) != len(mylist2):
            check = False
        else:
            arr = len(mylist1)
            for i in range(arr):
                if mylist1[i] != mylist2[i]:
                    check = False
                    break
    print(check)

mysum()
mysum(5)

mylist1 = [i for i in range(10, 51, 10)]
mylist2 = [i for i in range(10, 41, 10)]
equalsList(mylist1, mylist2)
equalsList(mylist1, mylist2, su=3)
equalsList(mylist1, mylist2, su=5)
