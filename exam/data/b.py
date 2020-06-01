import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False

def func(xdata):
    yd = [ np.log(x) for x in xdata]
    return yd
xdata = np.arange(1e-7, 100.0, 0.01)
ydata = func(xdata) # 함수 구현하세요.

plt.plot(xdata,ydata)
plt.show()

