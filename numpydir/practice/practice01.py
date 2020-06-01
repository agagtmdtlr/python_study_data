import numpy as np
arr = np.arange(1, 6)
print(sum(arr**(1/2)))
arr2 = np.array([[np.sum(arr),np.mean(arr),np.min(arr),np.max(arr)]])
print(arr2,type(arr2),arr2.shape)
arr3 = arr2.transpose()
print(arr3,type(arr3),arr3.shape)
print(np.matmul(arr2,arr3))
print(np.matmul(arr3,arr2))