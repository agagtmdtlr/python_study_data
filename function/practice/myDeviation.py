import math

def deviation(list1):
    # 평균
    avg = sum(list1)/len(list1)
    print(avg)
    # 평균편차 제곱 합
    total = sum([pow(i-avg,2) for i in list1])
    print(total)
    # 평균편차 제곱 평균
    dd = total/len(list1)
    print(dd)
    # 표준편차
    return math.sqrt(dd)

list1 = [10,30,40,80]
result = deviation(list1)
print(result)