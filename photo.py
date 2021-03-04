from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tkinter import filedialog
from tkinter import *

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2


def emotion_analysis(emotions):
    objects = ('angry','disgust','fear', 'happy', 'sad', 'surprise', 'neutral')
    x_pos = np.arange(len(objects))
    
    plt.bar(x_pos, emotions * 100, align='center', alpha=0.5)
    plt.xticks(x_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')

    cv2.namedWindow('Photo',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Photo', 500, 500)
    cv2.imshow('Photo',true_image)
    cv2.moveWindow('Photo',800,200)
    
    
    plt.show()
    

model = load_model('./models/model.h5')
model.summary()

root = Tk()
root.update()
file = filedialog.askopenfilename(initialdir = "/home/riderasg/amogh/8th Sem/major project/project/final",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
root.destroy()

true_image = cv2.imread(file)
img = image.load_img(file, color_mode = "grayscale", target_size=(48, 48))

x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)


custom = model.predict(x)
emotion_analysis(custom[0])

