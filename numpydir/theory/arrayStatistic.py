import  numpy as np

data = np.array([[10,20],[30,40]])
print(data)

print(np.sum(data))

# 0 : row (go down) , 1 : col (go right)
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))

print(np.mean(data, axis=0))
print(np.mean(data, axis=1))

print(np.min(data))
print(np.min(data, axis=0))
print(np.min(data, axis=1))

print(np.max(data))
print(np.max(data, axis=0))
print(np.max(data, axis=1))

print(np.cumsum(data))
print(np.cumsum(data, axis=0))
print(np.cumsum(data, axis=1))

print(np.cumprod(data))