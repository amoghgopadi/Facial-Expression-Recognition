import cv2
from model import FacialExpressionModel
import numpy as np

rgb = cv2.VideoCapture(0)
facec = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

def __get_data__():
    """
    __get_data__: Gets data from the VideoCapture object and classifies them
    to a face or no face. 
    
    returns: tuple (faces in image, frame read, grayscale frame)
    """
    _, fr = rgb.read()
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = facec.detectMultiScale(gray, 1.3, 5)
    
    return faces, fr, gray

def start_app(cnn):
    
    while True:
        faces, fr, gray_fr = __get_data__()
        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]
            roi = cv2.resize(fc, (48, 48))
            pred, prob = cnn.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            text = "%s , %.2f"%(pred,prob * 100)
            cv2.putText(fr, text, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)

        if cv2.waitKey(1) == 27:
            break
        cv2.imshow('WebCam', fr)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    model = FacialExpressionModel("./models/model.json", "./models/model.h5")
    start_app(model)

