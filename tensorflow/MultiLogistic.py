import numpy as np
import tensorflow.compat.v1 as tf
import tensorflow
tensorflow.compat.v1.disable_v2_behavior()

tensorflow.compat.v1.disable_v2_behavior()
# 입력 데이터
x_data = np.array([[2.0,3],[4,3],[6,4],[8,6],[10,7],[12,8],[14,9]])
# 출력 데이터
y_data=np.array([0.0, 0, 0, 0, 1, 1, 1]).reshape(7,1)

# 변수 노드
x = tf.placeholder(tf.float64, shape=[None,2])
y = tf.placeholder(tf.float64, shape=[None,1])

# tf.varibale 고정 변수
# random_normal : 표준 정규분포 값 seed : 난수 똑같이 나오게
w=tf.Variable(tf.random_normal([2,1], dtype=tf.float64, seed=0))
b=tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))

# 가설 함수
H= tf.sigmoid(tf.matmul(x,w) + b)

# 손실함수
diff = y*tf.log(H) + (1-y)*tf.log(1-H)
cost = -tf.reduce_mean(diff)

# 최적화 함수 정의
learn_rate = 0.1
optimizer = tf.train.GradientDescentOptimizer(learn_rate)

train = optimizer.minimize(cost)

# session에 모델 올리기
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# placeholder feed
train_dict = {x:x_data, y:y_data}

epochs = 50000+1
for step in range(epochs):
    sess.run(train,feed_dict=train_dict)
    if(step % 5000 == 0):
        _cost,_w,_b,_H = sess.run([cost,w,b,H],feed_dict=train_dict)
        print('step : %d' % (step))
        print('_cost : %f' % (_cost))
        print('_w : \n',_w)
        print('_b : \n',_b)
        print('가설 정보 : ')
        print(_H)
        print('-'*50)

# 0.5 확률값 비교 -> cast ( T, F ) return
predicted = tf.cast( H >= 0.5, dtype=tf.float64)
_predicted = sess.run(predicted,feed_dict=train_dict)

print('정답 : ', y)
print()
print('예측치 : \n',_predicted)
print()

accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,y), dtype=tf.float64))
_accuracy = sess.run(accuracy,feed_dict=train_dict)

print('정확도 :', _accuracy)
print()

# 점검용 데이터
x_test = np.array([[7,6],[6,3],[1,2]])
test_dict = {x:x_test}

_predicted = sess.run(predicted, feed_dict=test_dict)

print('합격 여부 :\n',_predicted)

sess.close()
print('finished')