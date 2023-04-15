import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

# Set Detector
detector = htm.handDetector(detectionConfidence=0.85)

# Set Capture Device
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# List of Drawing Colors
myListDirectory = os.listdir('Header')
# print(myListDirectory)
overlayList = []

for imPath in myListDirectory:
  image = cv2.imread(f'Header/{imPath}')
  overlayList.append(image)

# Set Header
header = overlayList[0]

while True:
  res, frame = cap.read()
  frame = cv2.flip(frame, 1)
  frame = detector.findHands(frame)
  frame[0: 125, 0: 1280] = header
  cv2.imshow('Video Feed', frame)
  if cv2.waitKey(10) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()