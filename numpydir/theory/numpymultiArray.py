import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a.shape)
#array[row,col]
newarr = a[[0,1,2],[0,1,0]]
print(newarr)
newarr2 = np.array([a[0,0],a[1,1],a[2,0]])
print(newarr2)

newarr3 = a[[1,2],[0,1]]
print(newarr3)

b = np.arange(25).reshape(5,5)
print(b)
print(b[range(5),range(5)])

arr = np.arange(1,13).reshape(4,3)
some = np.array([0,2,0,1])
arr[np.arange(4),some] += 5
print(arr)