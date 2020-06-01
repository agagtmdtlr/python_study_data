import numpy as np

arr01 = np.array([[1,2],[3,4]])
arr02 = np.array([[5,6],[7,8]])

result = np.concatenate((arr01,arr02))
print(result)

result = np.concatenate((arr01,arr02),axis=0)
print(result)

result = np.concatenate((arr01,arr02),axis=1)
print(result)