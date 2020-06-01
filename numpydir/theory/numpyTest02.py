import numpy as np
import matplotlib.pyplot as plt

xdata = np.arange(-np.pi , np.pi ,0.01)
print(xdata)

ydata = np.sin(xdata)
print(ydata)

plt.plot(xdata,ydata)

plt.show()