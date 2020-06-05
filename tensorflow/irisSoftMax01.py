import numpy as np
import matplotlib.pyplot as plt

import tensorflow
import tensorflow.compat.v1 as tf
tensorflow.compat.v1.disable_v2_behavior()

filename = 'iris_three.csv'
data = np.loadtxt(filename, delimiter=',', dtype=np.float32)
print(data.shape)

# 기초 변수
table_row = data.shape[0]
table_col = data.shape[1]

y_col = 1
x_col = table_col - y_col

test_row = 3
train_row = table_row - test_row

# 학습/테스트 데이터 분리 & input/output 데이터 분리
x_train = data[0:train_row,0:x_col]
y_train = data[0:train_row,x_col:]
x_test = data[train_row:,0:x_col]
y_test = data[train_row:,x_col:]

x = tf.placeholder(tf.float32, shape=[None,x_col])
y = tf.placeholder(tf.int32, shape=[None,y_col])

nb_classes = 3
# 주의 사항
# w의 column에는 클래스의 갯수
w = tf.Variable(tf.random_normal(shape=[x_col,nb_classes]))
b = tf.Variable(tf.random_normal(shape=[nb_classes]))

H = tf.nn.softmax(tf.matmul(x,w)+b)

# label data -> one hot encoding
y_one_hot = tf.one_hot(y, nb_classes)
# 차원 축소
y_one_hot = tf.reshape(y_one_hot, [-1, nb_classes])

# 손실함수
diff = -tf.reduce_sum(y_one_hot*tf.log(H),axis=1)
cost = tf.reduce_mean(diff)

learn_rate = 0.1
# 최적화 ( 손실함수 선택)
optimizer = tf.train.GradientDescentOptimizer(learn_rate)
train = optimizer.minimize(cost)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

epochs = 2000 + 1
train_dict = {x:x_train, y:y_train}

prediction = tf.argmax(H, axis=1) # 예측치
correct = tf.argmax(y_one_hot, axis=1) #

compare = tf.equal(prediction, correct) # 비교 결과 : return boolean list
casted = tf.cast(compare, tf.float32) # 진위 --> 숫자형 : change boolean to number : return float list
accuracy = tf.reduce_mean(casted) # 정확도




def inlineprint(H_list):
    imsi = ''
    for item in H_list:
        imsi += str(item) + ' '
    print(imsi)

# # 0(강아지), 1(고양이), 2(토끼)
def getCategory(datalist):
    mylist = ['강아지','고양이','토끼']
    for idx in range(len(datalist)):
        print(datalist[idx],mylist[int(datalist[idx])])

for step in range(epochs):
    _train = sess.run([train], feed_dict=train_dict)

    if (step % 200 == 0):
        _y_one_hot, _cost, _H = sess.run([y_one_hot, cost, H], feed_dict=train_dict)

        _prediction, _compare, _accuracy = \
            sess.run([prediction, compare, accuracy], feed_dict=train_dict)
        print('step : %d' % (step))
        print('_cost : %f' % (_cost))
        print('_accuracy : %f' % (_accuracy))
        print()
        print('예측 값')
        inlineprint(_prediction)
        print('_compare')
        inlineprint(_compare)
        print('가설')
        inlineprint(_H)
        print('-'*50)

test_dict = {x:x_test}

predict = sess.run(H, feed_dict = test_dict)
print('test_result')
test_result = np.argmax(predict, axis=1)

getCategory(test_result)

sess.close()



print('finished')