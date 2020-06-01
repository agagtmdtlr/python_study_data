import numpy as np

# 행렬
arrX = np.array([[1,2],[3,4]])
arrY = np.array([[5,6],[7,8]])

# 벡터
v = np.array([9,10])
w = np.array([11,12])

# 벡터의 내적
print(v.dot(w))
print(np.dot(v,w))

# 행렬과 벡터의 곱
print(np.dot(arrX,v))

# 행렬과 행렬의 곱
print(np.dot(arrX,arrY))

aaa = np.array([[1,2,3],[4,3,2]])
bbb = np.array([[1,0],[3,1],[0,3]])
print(aaa.shape)
print(bbb.shape)
print(np.dot(aaa,bbb))


ccc = np.array([[5,8],[9,3]])
ddd = np.array([[7,4],[7,5]])

result = np.add(ccc,ddd)
print(result)

result = np.divide(ccc, ddd)
print(result)