# string_test.pyy
# 문자열은 외따옴표 또는 쌍따옴표 모두 가능합니다.
food = "파이썬은 잼있는 언어입니다."
print(food)
print('-'*20)
food = 'hello world'
print(food)
print('-'*20)
food = "쌍따옴표 내에 '외따옴표' 가능"
print(food)
print('-'*20)
food = '외따옴표 내에 "쌍따옴표" 가능'
print(food)
print('-'*20)

# \n는 특수 문자(교재 48쪽)
food = '엔터키를 치려면 \\n을 누르시면 됩니다.'
print(food)
print('-'*20)

#쌍따옴표 3개로 멀티라인 문자열 편집을 할 수 있다.
multiline=""" 
    동해물과 백두사인 마르고 닳도록
    하느님이 보우하사 우리 나라 만세
"""
print(multiline)
print('-'*20)

#문자열 결합
head = 'Python'
tail = 'is fun'
result = head + tail
print(result)
print('-'*20)

#replication 문자열 반복
aaa = head * 10
print(aaa)
print('-'*20)

# 문자열 길이
length = len(aaa)
print(length)
print('-'*20)