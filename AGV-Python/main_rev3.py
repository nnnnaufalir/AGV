from cgi import print_arguments
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
from sys import path
from PathPlanning import PathPlanning
from MoveCalculation import MoveCalculation
from MoveSimulation import Simulation
import serial
import time

class Toolbox(PathPlanning, MoveCalculation, Simulation):
    pass

model = load_model('MobileNetV3S1023.h5')
classList = ['bigData', 'krai', 'uuesrg']
cam = cv2.VideoCapture(1 + cv2.CAP_DSHOW)

ser = serial.Serial('COM13',115200, timeout=1)
ser.flush()

a = Toolbox()
a.setState("A")
target="D"

run = a.pathPlanningStep(target,status=False)

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

counterA = 0
def rencana () :
    for i in range(len(run)):
        if i<1:
            path = str((run[counterA][0]))
            jarak = str((run[counterA][1]))
            derajat = str((run[counterA][2]))
            tujuan = str((run[counterA][3]))
    
    total =  '@' + path + ',' + jarak + ',' + derajat + ',' + tujuan + '$'
    return total

classVision = []
a = 0
counterA = 0
detek=False;
  
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        if line == "START KOMUNIKASI":
            #time.sleep(0.01)
            ser.write(b"READY\n")
            detek=True
        while detek == True :
            ser.write(b"" + predictVision().encode() + rencana().encode())
            line = ser.readline().decode('utf-8').rstrip()
            if line == "Plan Selesai":
                counterA += 1
            if line == "A":
                target="A"
            elif line == "B":
                target="B"
            elif line == "C":
                target="C"
            else : 
                counterA = 0
            print(target + " " + line)
