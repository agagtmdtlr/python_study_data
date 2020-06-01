import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# 상관계수 : correation
def correation(x, y):
    bar_x = x.mean()
    bar_y = y.mean()

    bunja = np.sum((x - bar_x)*(y- bar_y))
    print(bunja)

    left = np.sum((x-bar_x)**2)
    right = np.sum((y-bar_y)**2)
    bunmo = np.sqrt(left*right)
    print(bunmo)

    return bunja/bunmo

x = np.array([3, 5, 8, 11, 13])
y = np.array([1, 2, 3, 4, 5])

print(correation(x,y))
plt.xlabel('x')
plt.ylabel('y')

print(correation(x,y))
plt.scatter(x,y)
plt.show()

