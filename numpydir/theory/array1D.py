import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
# <class 'numpy.ndarray'>
print(type(arr))

print(arr[0][0],arr[0][1])

print(arr.ndim) # return demesion
print(arr.shape) # return structure 형상
print(arr.dtype) # return datatype
# 몇행이죠?
print(arr.shape[0])

arr[1][1] = 1234
print((arr.T))