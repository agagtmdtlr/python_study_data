import numpy as np
import math

array = np.array([1.57,2.48,3.93,4.33])
print(np.ceil(array))
print(np.floor(array))
print(np.round(array))
print(np.round(array,1))
print(np.sqrt(array))

arr = np.arange(10)
result = np.exp(arr)
print(result)

x = [5,4,9]
y = [6,3,6]
z = [1,2,3,4]
print(np.maximum(x,y)) # 같은 인덱스 끼리 비교
# print(np.maximum(y,z)) # error : 크기가 같아야함

arr1 = np.array([-1.1,2.2,3.3,4.4])
print(arr1)

arr2 = np.array([1.1,2.2,3.3,4.4])
print(arr2)

print(np.abs(arr1))
print(np.sum(arr1))
print(np.sum(np.abs(arr1)))
print(np.equal(arr1,arr2))
print(np.sum(np.equal(arr1,arr2)))
print(all(np.equal(arr1,arr2)))
# x = 6
# arr = [1,2,6]
# arr2 = np.array([1,2,6])
# print(id(x),id(arr), id(arr[2]),id(arr2), id(arr2[2]))
# print(x,arr[2],arr2[2])

arrX = np.array([[1,2],[3,4]],dtype=np.float64)
arrY = np.array([[5,6],[7,8]],dtype=np.float64)

print(arrX + arrY)
print(np.add(arrX,arrY))

print(arrX - arrY)
print(np.subtract(arrX,arrY))

print(arrX * arrY)
print(np.multiply(arrX,arrY))

print(arrX / arrY)
print(np.divide(arrX,arrY))

print(divmod(arrY,arrX))
print(np.divmod(arrY,arrX))

arr1 = np.array([-3,0,4])
arr2 = np.array([5,4,5])
print('-'*20)
print(np.sign(arr1)) # 부호 판단 양수:1 음수:-1 0:0
print(np.mod(arr1,arr2))

a = np.array([2,5,-1])
b = np.array([-1,4,3])
print(np.round(math.sqrt(np.sum(np.square(np.subtract(a,b)))),1))
print(np.round(math.sqrt(np.sum(np.square(np.subtract(a,b)))),1))
x = np.array([2,2,2])
y = np.array([1,2,3])
print(np.power(x,y))
print(np.power(y,3))