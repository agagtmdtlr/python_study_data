import  numpy as np

print(np.eye(3))

from pandas.core.series import Series
sdata = [20,30,40]
myseries2 = Series(sdata)

print(myseries2)

import  matplotlib.pyplot as plt
plt.plot([1,2,3,4],'b^--')
plt.title('graph')
plt.show()
print('finished')