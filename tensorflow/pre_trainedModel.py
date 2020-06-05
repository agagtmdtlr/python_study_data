from tensorflow.keras.applications.vgg16 import VGG16,preprocess_input,decode_predictions

from tensorflow.python.keras.preprocessing.image import load_img,img_to_array

model = VGG16()
model.summary()
# VGG16은 (224, 224, 3)

img_prefix = 'image/'
mylist = ['mydog.png','cat.jpg','myrabbit.jpg','fox.jpg']

import matplotlib.pyplot as plt

total_data =[]
for imgname in mylist:
    img = load_img(img_prefix + imgname, target_size=(224,224))
    plt.imshow(img)

    filename = img_prefix + '사전 학습 모델 '+ imgname
    plt.savefig(filename)
    print(filename + '으로 저장됨')

    img_arr = img_to_array(img) # (224,224)

    pre_input = preprocess_input(img_arr) # (224,224,3)
    print(pre_input.shape)
    total_data.append(pre_input)
# end for

import numpy as np

arr_input = np.stack(total_data)
print(arr_input.shape)

H = model.predict(arr_input)
print('H.shape : ', H.shape)

results = decode_predictions(H , top = 1)
print(results)
print(len(results))
print('-'*40)

print('finished')