import mediapipe as mp
import cv2
import pickle
import os
import matplotlib.pyplot as plt


DATA_DIR = './data'
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

for d in os.listdir(DATA_DIR):
    
    
    for img in os.listdir(os.path.join(DATA_DIR, d)):
        #data aus?

        x = []
        y = []

        print(os.path.join(DATA_DIR, d))
        print(os.path.join(DATA_DIR, d, img))

        image = cv2.imread(os.path.join(DATA_DIR, d, img))
        image - cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #detect landmarks in image(RGB format)
        results = hands.process(image)

        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks: #landmarks per image
                for i in hand_landmarks.landmark:
                    x.append(i.x)
                    y.append(i.y)

        

        