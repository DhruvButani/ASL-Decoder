import cv2 as cv
import mediapipe as mp
import pickle
import numpy as np



mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

model = pickle.load(open('./model.pickle', 'rb'))['model'] 

cap = cv.VideoCapture(0) 


labels = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'Z'}

while True:
    data_xy = []
    valid, image = cap.read()
    
    if not valid:
        print('Webcam could not be opened')
        break


    imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = hands.process(imageRGB)


    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks: #landmarks per image
               mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
    

        for hand_landmarks in results.multi_hand_landmarks: #landmarks per image
            for i in range(len(hand_landmarks.landmark)):
                data_xy.append(hand_landmarks.landmark[i].x)
                data_xy.append(hand_landmarks.landmark[i].y)


        ch = model.predict([np.asarray(data_xy)])
        cv.putText(image, labels[int(ch)], (250, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

         
    cv.imshow('Live Webcam',image)
    key = cv.waitKey(5)



    if key == ord('q'):
        print('Exiting')
        break

cap.release()
cap.destroyAllWindows()