import numpy as np
import tensorflow.compat.v1 as tf
import tensorflow
tensorflow.compat.v1.disable_v2_behavior()
# 입력 데이터
x=np.array([2.0, 4, 6, 8, 10, 12, 14])
# 출력 데이터
y=np.array([0.0, 0, 0, 0, 1, 1, 1])


# tf.varibale 고정 변수
# random_normal : 표준 정규분포 값 seed : 난수 똑같이 나오게
w=tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))
b=tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))

# 가설 함수
H=1/(1+np.e**(-w*x-b))

# 손실함수
diff = y*tf.log(H) + (1-y)*tf.log(1-H)
cost = -tf.reduce_mean(diff)

# 최적화 함수 정의
learn_rate = 0.5
optimizer = tf.train.GradientDescentOptimizer(learn_rate)
train = optimizer.minimize(cost)

# session에 모델 올리기
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

epochs = 50000+1
for step in range(epochs):
    sess.run(train)
    if(step % 5000 == 0):
        _cost,_w,_b,_H = sess.run([cost,w,b,H])
        print('step : %d' % (step))
        print('_cost : %f' % (_cost))
        print('_w : %f' % (_w))
        print('_b : %f' % (_b))
        print('가설 정보 : ')
        print(_H)
        print('-'*50)

# 0.5 확률값 비교 -> cast ( T, F ) return
predicted = tf.cast( H >= 0.5, dtype=tf.float32)
_predicted = sess.run(predicted)

print('정답 : ', y)
print()
print('예측치 : ',_predicted)
print()

accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,y), dtype=tf.float32))
_accuracy = sess.run(accuracy)

print('정확도 :', _accuracy)
print()

sess.close()
print('finished')