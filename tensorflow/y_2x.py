# y_2x.py
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# y=2x에 대한 학습
x_data = [1.0, 2, 3, 4]     # 입력
y_data = [2.0, 4, 6, 8]     # 출력

# 입력 데이터와 출력 데이터 준비
# placeholder 치환될 어떠한 값
x = tf.placeholder(tf.float32)  # 입력 데이터는 실수형 데이터 입니다.
y = tf.placeholder(tf.float32)  # 출력 데이터는 실수형 데이터 입니다.

# 가중치와 bias 정의
w = tf.Variable(tf.random_normal(shape=[1]))
b = tf.Variable(tf.random_normal(shape=[1]))
# y = wx + b > y = 2x : w = 2, b = 0 인 상태 ( but w 와 b 값은 모르는 상태 )
# tf.random_normal : 표준 정규 분포에 의해 random 값을 뽑아주는 함수

# 가설 정의
H = w*x + b

# 비용 함수 정의
diff = tf.square(H-y)
cost = tf.reduce_mean(diff)

# 옵티 마이저 정의 > 최적화를 하기위한 과정
learn_rate = 0.01  # 학습율
optimizer = tf.train.GradientDescentOptimizer(learn_rate)      # 경사 하강법
# 경사 하강법 : 1차 근삿값 발견용 최적화 알고리즘
# > 기본 개념은 함수의 기울기를 구하여 기울기가 낮은 쪽으로 계속 이동시켜서 극값에 이를때까지 반복하는 것이다.
train = optimizer.minimize(cost)
# 옵티마이저가 비용 함수를 이용하여 최적화된 결과물을 만들어준다.


# 세션 변수 정의
# 세션 : 텐서 플로우가 연산 작업을 수행하는 영역 (공간)
sess = tf.Session()     # 세션 객체 생성
init = tf.global_variables_initializer()    # 세션 공간 초기화 객체
sess.run(init)

# epoch 수만큼 반복 실행
# epoch : 위의 코딩을 반복하는 횟수(에포크) > 반복하다보면 잔차 제곱의 합을 줄여주고, 그만큼 0에 가까워짐
epochs = 10000+1
for step in range(epochs) :
    sess.run(train, feed_dict={x:x_data, y:y_data})
    if (step % 1000 == 0) :
        # 만번을 반복하되 1000번 단위로 출력하여 보겟다 ( 디테일 하게 볼꺼면 1000>10 이런식으로 줄이면 됨)
        _cost, _w, _b, _H = sess.run([cost, w, b, H], feed_dict={x:x_data, y:y_data})
        print('epoch : %d' % (step))
        print('_cost : %d' % (_cost))
        print('_w : %d' % (_w))
        print('_b : %d' % (_b))
        print('_H : \n', _H)
        print('--------------------------------------')

# sess.run([tensor], feed_dict= 집어 넣어주는 값 > 사전 형식으로 넣어주세요 )
# x에는 x_data가 치환됩니다.
# sess.run : sess 작업 공간에 내용물 넣고 러닝
# 파이썬 공간으로 빼려면 변수로 빼냅니다(_cost, _w, _b, _H) > 파이선 변수 형식
# cost, w, b, H > 텐서 형식


# 테스터 데이터로 예측하기
x_test = [3.5, 5, 5.5, 6]    # 점검용 데이터

print(sess.run(H, feed_dict={x:x_test}))
sess.close()

print('finish')