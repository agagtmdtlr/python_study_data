import math
import matplotlib.pyplot as plt
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense,Conv2D,Flatten,Dropout # 레이어 추가
# 이미지 증식
idg = ImageDataGenerator(
    rescale=1/255, # 스케일 변경
    rotation_range=90.0, # 회전 각도
    width_shift_range=1.0, # 수평 방향 이동 비율
    height_shift_range=0.5, # 수직 방향 이동 비율
    shear_range=0.8, # 반시계 방향의 전단 강도(radian)
    zoom_range=0.5, # 랜덤하게 확대할 사진의 범위 지정
    horizontal_flip=True, # 수평 방향으로 입력 반전
    vertical_flip=True # 수직 방향으로 입력 반전
)

print(idg)

target_w, target_h, col_mode = 512, 512, 3 # 너비, 높이, 컬러 모드

# 이미지가 들어있는 폴더를 접근하여 이미지 가져 오기
iters = idg.flow_from_directory(directory='img',target_size=(target_w,target_h),\
                               classes=['sampleA','sampleB'],color_mode='rgb',\
                               class_mode='binary',batch_size=4,shuffle=False)

print(type(iters))
print('-'*50)

print(iters.batch_size)
print('-'*50)

print(iters.image_shape)
print('-'*50)

# next() : 1회 batch 분의 데이터를 취득합니다
x_train,y_train = next(iters)
print( len(x_train))
print('-'*50)
print( len(y_train))
print('-'*50)
print(x_train.shape)
print('-'*50)
print(y_train.shape)
print('-'*50)

plt.axis('off')
for idx in range(len(x_train)):
    plt.imshow(x_train[idx])
    filename = 'image/image_gen' + str(idx) + '.png'
    plt.savefig(filename)

model = Sequential()
model.add(Conv2D(16,(3,3),input_shape=(target_w,target_h,col_mode)))
model.add(Flatten())
model.add(Dense(32,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='rmsprop')

epochs = math.ceil(iters.samples/5)
print(iters.samples)
# steps_per_epoch : 에포크 당 배치 횟수
history = model.fit_generator(iters,steps_per_epoch=epochs)
