#케라스를 이용한 선형 회귀
import numpy as np

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

# y = 2 * x + 1

x = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
y = np.array([3.1, 1.1, 4.9, 6.1, 6.9, 8.2, 9.1])

# 모델 만들기
# 머신 러닝을 위한 모델을 만들어 주는 클래스, 시퀀셜
model = Sequential()

# 각 레이어에 구조 만들기
# input_dim : input 의 차원수
# units : output의 차원수
model.add(Dense(units=1, input_dim=1))

from tensorflow.python.keras import optimizers
# 컴파일
sgd = optimizers.SGD(lr=0.1) # lr은 학습률을 말한다.
# optimizer ) 옵티마이저
# loss) cost function
model.compile(optimizer=sgd, loss='mse')

model.summary()

# 모델을 실습시키는 메소드
model.fit(x,y, epochs=200)

# 예측
predict = model.predict(x=np.array([5.0]))

print(predict)
print('-'* 40)

# 가중치
# [array([[2.4403093]], dtype=float32), array([-0.47130808], dtype=float32)]
print(model.get_weights())
print('-'* 40)

print(model.get_config())
print('-'* 40)

print('finished')


