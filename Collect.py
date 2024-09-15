import cv2 as cv
import os


# Per letter take 100 pictures
# Take 100 pictures per everytime s is pressed
# 
#
#
cap = cv.VideoCapture(0) #0 is default webcam

DIR = './data'

datasize = 100
signals = 36
images = 0


for uploaded in range(36):

    b = True
    while(images <26):
        valid, image = cap.read()
        
        if not valid:
            print('Webcam could not be opened')
            break

        cv.putText(image, 'Press s to start capturing, q to quit', (250, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
        cv.imshow('Live Webcam',image)
        key = cv.waitKey(1)

        if  key == ord('q'):
            print('Exiting')
            b = False
            break
        
        if key == ord('s'):
            print('Capturing')
            break

    if not b:
        break
    
    os.mkdir(DIR + '/' + str(images))
    uploaded = 0

    while(uploaded<datasize):
        valid, image = cap.read()

        if not valid:
            print('Webcam could not be opened')
            break

        cv.imshow('Live Webcam',image)
        print(uploaded)

        cv.waitKey(25)
        cv.imwrite(DIR + '/' + str(images) + '/' + str(uploaded)+'.png', image)
        uploaded += 1


    print('Done Uploading '+str(images))

    key = True
    uploaded = 0
    images += 1


cap.release()
cv.destroyAllWindows()