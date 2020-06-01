import numpy as np

arr = np.random.permutation(np.arange(1,46))[:7]
print(f'1등 : {np.sort(arr[:6])} 2등 번호 : {arr[-1]}')

arr = np.random.choice(np.arange(1,46),7,replace=False)
print(f'1등 : {np.sort(arr[:6])} 2등 번호 : {arr[-1]}')

temp = np.random.permutation(np.arange(16)).reshape(4,4)
temp2 = np.random.permutation(np.arange(16).reshape(4,4))
print(temp)
print(temp2)

import numpy as np

x = np.array([3,6])
y = np.array([1,4])
print(np.dot(x,y))
print(np.matmul(x,y))