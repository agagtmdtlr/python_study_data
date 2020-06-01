import numpy as np
import tensorflow.compat.v1 as tf
import tensorflow
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense # 레이어 추가
from tensorflow.python.keras.optimizers import SGD

tensorflow.compat.v1.disable_v2_behavior()


# 입력 데이터
x_data = np.array([[2.0,3],[4,3],[6,4],[8,6],[10,7],[12,8],[14,9]])
# 출력 데이터
y_data=np.array([0.0, 0, 0, 0, 1, 1, 1]).reshape(7,1)

model = Sequential() # 모델 객체 생성

# input이 2개이고 , output은 1개 입니다.
# activation은 활성화 함수를 지정하는 옵션
model.add(Dense(units=1, input_dim=2, activation='sigmoid'))
# optimizer : 최적화 함수
# loss : 손실함수
learn_rate=0.1 # 학습률
sgd = SGD(lr=learn_rate)
# optimizer = 'sgd' 는 learn rate 를 default값 밖에 못씀
model.compile(optimizer=sgd,loss='binary_crossentropy') # 컴파일

model.fit(x=x_data,y=y_data,epochs=2000,verbose=1) # 훈련

x_test = [[2,1],[6,5],[11,6]]

# 데이터 하나씩 예측하기 : class 0 , 1
# logistic method => predic_classes()
# ge

pred = model.predict_classes(np.array(x_test))
print(pred)