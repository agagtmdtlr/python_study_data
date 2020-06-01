import numpy as np

arr = np.arange(1,17).reshape(4,4)
print(arr)
arr2 = arr[0::2,1:4]
print(arr2)
arr3 = arr[1::2,0:3]
print(arr3)
arr3T = arr3.transpose()
print(arr3T)
print(np.matmul(arr2,arr3T))
print(np.matmul(arr3T,arr2))
