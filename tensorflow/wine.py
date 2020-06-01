'''
preprocessing
callbacks에 대한 개념 공부
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder # 라벨 인코딩

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import load_model # 학습 모델 정장
from tensorflow.keras import optimizers as opt
from tensorflow.keras import losses as los
from tensorflow.keras import activations as act
from tensorflow.keras import callbacks

filename = 'wine.csv'
df_wine = pd.read_csv(filename,header = None)

df = df_wine.sample(frac=0.15)

data = df.values

total_col = data.shape[1] # 전체 컬럼수
y_column = 1 # classes / output atrs number
x_column = total_col - y_column # input atrs number

# seperate dataset : input , output
x = data[:, 0:x_column]
y = data[:, x_column:]

model = Sequential()

# graph 세팅
# x_column :
# add : relu 중간 단계에 많이 씀
model.add(Dense(units=30, input_dim=x_column,activation=act.relu))
model.add(Dense(units=10,activation='relu'))

# print(model.summary())
# ouput layer
model.add(Dense(units=y_column, activation='sigmoid'))
# print(model.summary())
# 기법 선택
model.compile(optimizer=opt.Adam(),loss=los.mean_squared_error,metrics=['accuracy'])

import os

model_dir = './model/'
if not os.path.exists(model_dir):
    os.mkdir(model_dir)

# loss : cost function 훈련 데이터에 대한 손실함수 결과
# val_loss : 훈련 검증 데이터의 손실값
model_name = './model/{epoch:02d}-{val_loss:.4f}.hdf5'
mcp = callbacks.ModelCheckpoint(filepath=model_name,monitor='val_loss',save_best_only=True)
es = callbacks.EarlyStopping(monitor='val_loss',patience=100)

# 학습 learning
# validation_split : 훈련 데이터중에서 %만 검증 데이터로 사용 옵션
# 각 epoch의 끝에서 손실과 다른 metrics를 평가하는데 사용
history = model.fit(x,y,validation_split=0.2, epochs=500, batch_size=100, verbose=0, callbacks=[es,mcp])
# model learning time log
val_loss = history.history['val_loss']

accuracy = history.history['accuracy']

x_len = np.arange(len(accuracy))
plt.plot(x_len,val_loss,'o',C='red',markersize=3)
plt.plot(x_len,accuracy,'o',C='blue',markersize=3)

plt.show()
