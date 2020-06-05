import numpy as np
import matplotlib.pyplot as plt

import tensorflow
import tensorflow.compat.v1 as tf
tensorflow.compat.v1.disable_v2_behavior()

# input data
x_data = [[1,2,1,1],[2,1,3,2]] # dim : 2 ,4
# 3 classes output data : cat 0,1,2
# 0, 1, 2의 3가지 종류가 있는 종속 변수
y_data = [[2],[1]] # dim : 2 , 1

x_col = len(x_data[0])
y_col = len(y_data[0])

nb_classes = 3 # 클래스의 갯수

x = tf.placeholder(tf.float32, shape=[None,x_col])
y = tf.placeholder(tf.int32, shape=[None,y_col])

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

cost_list = [] # 비용결과 저장


epochs = 2000 + 1
train_dict = {x:x_data, y:y_data}

def inlineprint(H_list):
    imsi = ''
    for item in H_list:
        imsi += str(item) + ' '
    print(imsi)

# 0(강아지), 1(고양이), 2(토끼)
def getCategory(datalist):
    mylist = ['강아지','고양이','토끼']
    for idx in range(len(datalist)):
        print(datalist[idx],mylist[int(datalist[idx])])
for step in range(epochs) :
    _train, _cost, _H, _w = sess.run([train,cost,H,w], feed_dict = train_dict)
    cost_list.append(_cost)
    if(step % 500 == 0):
        print('step : %d' % (step))
        print('가설 정보')
        inlineprint(_H)
        _answer = np.argmax(_H, axis=1)
        print('argmax :', _answer)
        getCategory(_answer)
        print('-'*40)

plt.plot(cost_list)
plt.show()
sess.close()



print('finished')