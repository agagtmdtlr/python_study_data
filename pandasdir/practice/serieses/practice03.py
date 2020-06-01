import random
import numpy as np
from pandas import Series

# lists1 = [random.randint(1,10) for i in range(10)]
# lists2 = [random.randint(1,10) for i in range(10)]
# series1 = Series(concat_data=lists1)
# series2 = Series(concat_data=lists2)
# print(series1)
# print(series2)
# arr1 = np.random.randint(1,11,size=10)
# arr2 = np.random.randint(1,11,size=10)
arr1 = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([9,8,7,6,5,4,3,2,1])
series1 = Series(data=arr1)
series2 = Series(data=arr2)
# print(series1)
# print(series2)

print(series1.lt(series2)) #less than series1 < series2