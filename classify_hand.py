import cv2  
import csv
import mediapipe as mp
import knn_neighbors
import numpy as np
import distance_angle_defs

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Sets up video capture device

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mpDraw = mp.solutions.drawing_utils
model = knn_neighbors.generate_model() #Creates a KNN model for classifying hand data

prediciton_mode = True # If writing data to file, False. If retying to predict, True
TARGET_LETTER = "U" # Only matters if prediciton_mode = False. Target letter tring to write data for

while True:
    success, img = cap.read() #Creates and image from the successfully captured camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Mediapipe needs RGB Values, so have to convert
    results = hands.process(imgRGB) #Mediapipe sets result to values of hand landmarks if found, and None if not

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0] #Only doing one hand, but needs to convert pull the hand from a tuple
        hand_landmarks = [] #Empty List to add data to     
        h, w, c = img.shape

        for id, lm in enumerate(hand.landmark): #Goes through every single landmark found
            cx, cy = int(lm.x * w), int(lm.y * h)
            hand_landmarks.append([id, cx, cy]) #Adds landmark ID, X, and Y to list. Used to get distances and angles later

        distances = distance_angle_defs.get_hand_distances(hand_landmarks)
        angles = distance_angle_defs.get_angles(hand_landmarks)
        data = distances + angles #List addition. Concats the distances and angles list into 1 list.

        if (prediciton_mode): #Want to predict the letter
            prediciton = model.predict(np.array(data).reshape(1, -1)) #Uses model to classify given hand data to letter
            cv2.putText(img, str(prediciton), (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3) #Writes the predicted letter to the screen

        else: # Want to write hand data
            data.append(TARGET_LETTER)
            with open("hand_data.csv", "a") as hd: #Appends the data with the target letter to csv
                writer = csv.writer(hd, lineterminator='\n')
                writer.writerow(data)
            
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS) #Draws all of the connections and landmarks onto hand

    cv2.imshow("Image", img)
    cv2.waitKey(1)