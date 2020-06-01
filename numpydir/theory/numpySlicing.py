import numpy as np
import copy
list1 = [idx for idx in range(10)]
print(list1)

arr1 = np.array(list1)
print(arr1)
print(arr1[5])
print(arr1[5:8])
print(arr1[1:7:2])
arr1[5:8]=12
arr_slice = arr1[5:8]
arr_slice[1]=100
print(arr1)

arr_slice = copy.deepcopy(arr1[5:8])
arr_slice[1]=200
print(arr1)

arr2 = np.arange(16).reshape(4,4)
arr_slice2 = copy.deepcopy(arr2)
arr_slice2[1] = 10
print(arr2)
print(arr_slice2)


# print(id(list1),id(list1[9]))
# list1.append(6)
# print(id(list1[10]))
# list1.append(6)
# list1.append(6)
# print(id(list1[11]))
#
# print(id(arr1),id(arr1[6]))

# shape(2,2,3)

# shape(3,3,2)
arr3 = np.array([[[1,1],[1,1],[1,1]],[[1,1],[1,1],[1,1]],[[1,1],[1,1],[1,1]]])
print(arr3.shape)