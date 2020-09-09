import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while 1:
    check, frame = cap.read()
    cv2.imshow('Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break