import numpy as np

arr1 = np.array([1,2,3],dtype=np.float)
print(arr1.dtype)

arr2 = np.array([1,2,3],dtype=np.int) # 암묵적으로 dtype 처리를 해줌
print(arr2.dtype)
float_arr = arr2.astype(np.float64)
print(float_arr.dtype)

arr3 = np.array([1.1,2.4,3.7],dtype=np.float)
print(arr3.dtype)

int_arr4 = arr3.astype(np.int)
print(int_arr4)

# np.string_
arr5 = np.array(['1.25','-9.6'], dtype=np.string_)
print(arr5.dtype)
print(arr5)

num_arr = arr5.astype(np.float)
print(num_arr)
