import matplotlib.pyplot as plt
from tensorflow.python.keras.datasets import mnist

(x_train, y_train) , (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

digit = x_train[4]
print(digit)
plt.imshow(digit)
print()
plt.show()