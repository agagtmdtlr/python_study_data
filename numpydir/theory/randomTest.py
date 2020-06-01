import numpy as np

result = np.random.random((2,2)) # [0~1)
print(result)

result = np.random.random_integers(1,10,(2,2)) # low,hing
print(result)

# 정규 분포 : 평균 0이고,분산이 1인 정규 분포에 표본 추출
result = np.random.randn(2,3)
print(result)

result = np.random.rand(4,4)
print(result)

result = np.random.randint(5,size=(3,3))
print(result)

# 주사위를 5번 던져서 나오는 수의 총합 구하기
result = np.sum(np.random.randint(1,7,size=5))
print(result)

length = 5
result = np.random.permutation(length) # integer : x
print(result)
arr = np.arange(16).reshape(4,4)
result = np.random.permutation(arr) # arrays : x
print(result)

# np.random.normal(평균, 표준편차, 사이즈)
print(np.random.normal(0, 0.01, 10))
print(np.random.normal(25,10,(2,2)))

# np.random.choice(np.arange(a),size=None,replace,p=None)
result = np.random.choice(5)
print(result)

result = np.random.choice(5,3)
print(result)

result = np.random.choice(5,300,p=[0.1,0,0.6,0,0.3])
print(result)
