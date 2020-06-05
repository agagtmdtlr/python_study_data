import numpy as np
import matplotlib.pyplot as plt

import tensorflow
import tensorflow.compat.v1 as tf
tensorflow.compat.v1.disable_v2_behavior()

from tensorflow.python.keras import losses
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense,Activation # 레이어 추가
from tensorflow.python.keras.optimizers import SGD
filename = 'soft_sample_01.csv'
data = np.loadtxt(filename, delimiter=',', dtype=np.float32)

# print(data.shape)

# 기초 변수 정의
table_row = data.shape[0]
table_col = data.shape[1]

# 슬라이싱 col 개수 정의
y_col = 1
x_col = table_col - y_col

nb_classes = 3

x_train = data[0:table_row,0:x_col]

y_train = data[0:table_row,x_col:]
# one hot encoding
y_train = np_utils.to_categorical(y_train, nb_classes, dtype='float32')

model = Sequential()

model.add(Dense(units=nb_classes,input_shape=(4,)))
model.add(Activation('softmax'))

model.compile(loss=losses.categorical_crossentropy,optimizer=SGD(),metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=1000, verbose=0)
print(history)
print('-'*50)

x_test = [[1,2,1,1],[1,2,5,6]]

for item in x_test:
    prediction = model.predict_classes(np.array([item]))
    print(prediction)
    H = model.predict(np.array([item]))
    print('가설 정보')
    print(H)
    print('-'*50)

print(model.predict_classes(np.array(x_test)))
print(model.predict(np.array(x_test)))
print('finished')