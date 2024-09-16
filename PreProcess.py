import mediapipe as mp
import cv2
import pickle
import os
import matplotlib.pyplot as plt


DATA_DIR = './data'
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

data = []
labels = []

for d in os.listdir(DATA_DIR):
    

    for img in os.listdir(os.path.join(DATA_DIR, d)):
        data_xy = []


        print(os.path.join(DATA_DIR, d))
        print(os.path.join(DATA_DIR, d, img))

        image = cv2.imread(os.path.join(DATA_DIR, d, img))
        image - cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #detect landmarks in image(RGB format)
        results = hands.process(image)

        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks: #landmarks per image
                for i in range(len(hand_landmarks.landmark)):
                    data_xy.append(hand_landmarks.landmark[i])
                    data_xy.append(hand_landmarks.landmark[i])

        

            data.append(data_xy)
            labels.append(d)

f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels},f)  
f.close()