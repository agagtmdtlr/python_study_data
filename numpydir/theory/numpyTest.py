import numpy as np
import matplotlib.pyplot as plt

xdata = np.arange(-10.0 , 10.0 ,0.01)
print(xdata)

ydata = np.e ** xdata
print(ydata)

plt.plot(xdata,ydata)

plt.show()