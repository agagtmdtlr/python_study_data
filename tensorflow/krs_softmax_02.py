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

# separate dataset input/out train/test
def getDataSet(data,testing_row=5,one_hot=False,num_classes=0):
    # 기초 변수 정의
    table_row = data.shape[0]
    table_col = data.shape[1]

    training_row = table_row - testing_row

    # 슬라이싱 col 개수 정의
    y_col = 1
    x_col = table_col - y_col

    x_train = data[0:training_row, 0:x_col]
    y_train = data[0:training_row, x_col:]

    x_test = data[training_row:,0:x_col]
    y_test = data[training_row:,x_col:]

    if one_hot:
        # one hot encoding
        y_train = np_utils.to_categorical(y_train, nb_classes, dtype='float32')

    return x_train,x_test,y_train,y_test
# end def getDataSet

if __name__ == '__main__':
    filename = 'softmax02.csv'
    data = np.loadtxt(filename, delimiter=',', dtype=np.float32)

    nb_classes = 3
    x_train, x_test, y_train, y_test = getDataSet(data,testing_row=2,one_hot=True,num_classes=nb_classes)

    model = Sequential()

    model.add(Dense(units=nb_classes,input_shape=(x_train.shape[1],)))
    model.add(Activation('softmax'))

    model.compile(loss=losses.categorical_crossentropy,optimizer=SGD(),metrics=['accuracy'])

    history = model.fit(x_train, y_train, epochs=1000, verbose=0)
    print(history)
    print('-'*50)

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