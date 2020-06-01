import random
def lotto(su):
    total = list()
    for i in range(su):
        set1 = set()
        list1 = list()
        while True :
            temp = random.randint(1,45)
            set1.add(temp)
            if len(set1) == 6 :
                list1 = sorted(set1) # 리스트 형태 봔화
            if len(set1) == 7 :
                list1 = [(list1,temp)]
                print(f'{i+1}게임 로또번호 : {list1}')
                total.append(list1)
                break
        #end while
    #end for
    return total
#end function

total = lotto(5)
print('\n'.join(map(str,total)))
print(total)