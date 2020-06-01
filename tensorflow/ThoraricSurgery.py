import numpy as np

from sklearn.model_selection import train_test_split

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

filename = 'ThoraricSurgery.csv'

data = np.loadtxt(filename, delimiter=',')
print(data.shape)

total_col = data.shape[1] # 전체 컬럼수
y_column = 1 # classes / output atrs number
x_column = total_col - y_column # input atrs number

# seperate dataset : input , output
x = data[:, 0:x_column]
y = data[:, x_column:]

# seperate dataset : traint , test
seed = 0
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=seed,shuffle=True)

model = Sequential()
# x_column :
# add : relu 중간 단계에 많이 씀
model.add(Dense(units=30, input_dim=x_column,activation='relu'))
# ouput layer
model.add(Dense(units=y_column, activation='sigmoid'))


model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=30, batch_size=10, verbose=1)

eval = model.evaluate(x_train,y_train)
print('loss : %.4f' %(eval[0]))
print('accuracy : %.4f' %(eval[1]))

pred = model.predict_classes(x_test)
for idx in range(len(pred)):
    label = y_test[idx]
    # print(label)
su = np.sum( pred == y_test)
print(su,np.size(y_test))
print(model.metrics_names)
import tensorflow as tf

print(tf.keras.optimizers.Adam)
print(tf.keras.losses)
print(tf.keras.activations)

eval = model.evaluate(x_test,y_test)
print('loss : %.4f' %(eval[0]))
print('accuracy : %.4f' %(eval[1]))