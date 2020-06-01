# map 함수 : map(함수,iterable)
#     iterable 객체를 '함수'에 넣어서 결과를 묶어 반환해줍니다.

print('# 일반함수 사용')
def two_times1(mylist):
    result = []
    for num in mylist :
        result.append(2*num)
    return result

somelist = [1,2]
result = two_times1(somelist)
print(result)

print('# map 함수 사용')
def two_times2(number):
    return  2*number

newlist = list(map(two_times2,somelist))
print(newlist)

print('# lambda와 map 함수 같이 사용')
newlist2 = list(map(lambda x : 2*x,somelist))
print(newlist2)