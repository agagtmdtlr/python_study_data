import numpy as np

a = np.array([-1,3,2,-6])
b = np.array([3,6,1,2])

A = np.reshape(a, [2,2])
print(A)

B = np.reshape(b,[2,2])
print(B)

# matrix multiply
result = np.matmul(A,B)
print(result)

result = np.matmul(B,A)
print(B)

a = np.reshape(a,[1,4])
b = np.reshape(b,[1,4])
print(a)
print(b)

b2 = np.transpose(b)
print(b2)

result = np.matmul(a,b2)
print(result)