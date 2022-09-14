import serial
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
import time

model = load_model('MobileNetV3S1023.h5')
classList = ['bigData', 'krai', 'uuesrg']
cam = cv2.VideoCapture(1)

def predictVision():
    check, frame = cam.read()

    cv2.imshow('video', frame)

    frame = cv2.resize(frame, (224, 224))
    img_array = image.img_to_array(frame)
    img_batch = np.expand_dims(img_array, axis=0)

    prediction = np.argmax(model.predict(img_batch), axis=-1)
    # print(classList[prediction[0]])
    # time.sleep(0.01)

    key = cv2.waitKey(1)

    return classList[prediction[0]]

classVision = []
a = 0

while True:
    print(predictVision())
#kirim = predictVision()
# while True :
#     print(predictVision())
# def finalPredictVision():
#     global a
#     global classVision
#     if len(classVision)<=5:
#         classVision.append(predictVision())
#     elif len(classVision)>5:
#         classVision.pop(0)
#     a+=1
#     if a == 5:
#         print(max(classVision))
#         a = 0
# while True:
    # print(str(predictVision()))
# if __name__ == '__main__':
# ser = serial.Serial('COM13',115200, timeout=1)
# ser.flush()

# while True:
#     # if ser.in_waiting > 0:
#     kirim = str(predictVision()) + '#'
#     #rencana()
#     line = ser.readline().decode('utf-8').rstrip()
#     # print(kirim)
#     ser.write(b"" + kirim.encode())
#             #print(rencana())
#             # if line == "START KOMUNIKASI":
#             #     print("OKE")
#             # if line == "Path Selesai":
#             #     counterA +=1
#             #ser.write(b"" + rencana().encode())
#         #print(tf.__version__)
#         #finalPredictVision()
