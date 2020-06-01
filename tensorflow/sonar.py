import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder # 라벨 인코딩

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import load_model # 학습 모델 정장
from tensorflow.keras import optimizers as opt
from tensorflow.keras import losses as los
from tensorflow.keras import activations as act
from tensorflow.keras import callbacks

filename = 'sonar.csv'
df = pd.read_csv(filename,header = None)

print(np.shape(df))
print(df.info())
print(df[60].unique())
data = df.values

total_col = data.shape[1] # 전체 컬럼수
y_column = 1 # classes / output atrs number
x_column = total_col - y_column # input atrs number

# seperate dataset : input , output
x = data[:, 0:x_column]
y_imsi = data[:, x_column:]

# encoding instance
e = LabelEncoder()
e.fit(y_imsi)
y = e.transform(y_imsi)

# seperate dataset : traint , test
seed = 0
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=seed,shuffle=True)

x_train = x_train.astype(np.float)
x_test = x_test.astype(np.float)
y_train = y_train.astype(np.float)
y_test = y_test.astype(np.float)

model = Sequential()

# graph 세팅
# x_column :
# add : relu 중간 단계에 많이 씀
model.add(Dense(units=30, input_dim=x_column,activation=act.relu))
model.add(Dense(units=10,activation='relu'))

# ouput layer
model.add(Dense(units=y_column, activation='sigmoid'))

# 기법 선택
model.compile(optimizer=opt.Adam(),loss=los.mean_squared_error,metrics=['accuracy'])
# 학습
model.fit(x_train,y_train, epochs=30, batch_size=10, verbose=1)

model.save('my_model.h5')

del model

model = load_model('my_model.h5')


print(model.metrics_names)
eval = model.evaluate(x_test,y_test)
print(eval)