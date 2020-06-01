import numpy as np

result = np.random.permutation(45)[:7]
second = result[-1]
result = np.sort(result)
print('금주 로또 번호')
print(result)


print('이등 번호')
print(second)