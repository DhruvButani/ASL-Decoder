import cv2 as cv
import os


# Per letter take 100 pictures
# Take 100 pictures per everytime s is pressed
# 
#
#
cap = cv.VideoCapture(0) #0 is default webcam

DIR = './data'

datasize = 200
signals = 36
images = 0


for uploaded in range(36):

    b = False
    while(True):
        valid, image = cap.read()
        
        if not valid:
            print('Webcam could not be opened')
            break
        cv.imshow('Live Webcam',image)

        if cv.waitKey(1) == ord('q'):
            print('Exiting')
            b = True
            break

        if cv.waitKey(1) == ord('s'):
            print('Capturing')
            break

    if not b:
        break

    uploaded = 0
    while(uploaded<datasize):
        valid, image = cap.read()
        if not valid:
            print('Webcam could not be opened')
            break
        cv.imshow('Live Webcam',image)

        cv.waitKey(25)
        cv.imwrite(folder=, img=image, )






    

cap.release()
cv.destroyAllWindows()