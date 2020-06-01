import re
def DashInsert(strings):
    mylist = [int(i) for i in strings]
    i = 0
    result = ''
    while True :
        result += str(mylist[i])
        if i+1 == len(mylist): # 현재 인덱스와 그다음 인덱스를 비교해야 되는다 마지막 인덱스는 그다음 비교 데이터가 없으므로 탈출
            break
        if mylist[i]%2 == 0:
            if mylist[i+1]%2 == 0:
                result += '*'
        else:
            if mylist[i + 1] % 2 != 0:
                result += '-'
        i += 1
    return result

inputdata = input('입력 : ')
result = DashInsert(inputdata)
print(f'결과 : {result}')