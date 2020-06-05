from tensorflow.keras.applications.resnet import ResNet50,ResNet101,ResNet152,preprocess_input,decode_predictions

from tensorflow.python.keras.preprocessing.image import load_img,img_to_array

model = ResNet152()
model.summary()
