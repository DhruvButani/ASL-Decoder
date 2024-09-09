import cv2 as cv
import os



if 

cap = cv.VideoCapture(0) #0 is default webcam

if cap.isOpened is True:
    print('Webcam could not be opened')
    exit()

while(True):
    valid, image = cap.read()
    
    if not valid:
        print('Webcam could not be opened')
        break

    cv.imshow('Live Webcam',image)

    if cv.waitKey(1) == ord('s'):
        while(True):



    if cv.waitKey(1) == ord('q'):
        print('Exiting')
        break



cap.release()
cv.destroyAllWindows()