import numpy as np

su1 = 2
rep_cnt = 5

result = np.repeat(su1,rep_cnt)
print(result)

# 값 3을 가진 요소가 4개인 배열 만들기
su2 = 3
rep_cnt2 = 4
result = np.repeat(su2,rep_cnt2)
print(result)

abcd = np.repeat(su1,rep_cnt)
defg = np.repeat(su2,rep_cnt2)
result = np.concatenate((abcd,defg))
print(result)

# 1은 100개, 3은 50의 배열을 만들고, 총합 구하기
result = np.sum(np.concatenate((np.repeat(1,100),np.repeat(3,50))))
print(result)