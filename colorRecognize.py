import cv2
import numpy as np

width = 410
height = 410
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
cap.set(10, 150)

def escape(x):
    pass

cv2.namedWindow("settingOfImage")
cv2.resizeWindow("settingOfImage",500,300)
cv2.createTrackbar("Min Ton", "settingOfImage", 0, 179, escape)
cv2.createTrackbar("Max Ton", "settingOfImage", 179, 179, escape)
cv2.createTrackbar("Min Doy", "settingOfImage", 0, 255, escape)
cv2.createTrackbar("Max Doy", "settingOfImage", 255, 255, escape)
cv2.createTrackbar("Min Val", "settingOfImage", 0, 255, escape)
cv2.createTrackbar("Max Val", "settingOfImage", 255, 255, escape)
#cv2.createTrackbar("reset", "settingOfImage", 0, 1, escape)


while True:
    check, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    minTon = cv2.getTrackbarPos("Min Ton", "settingOfImage")
    maxTon = cv2.getTrackbarPos("Max Ton", "settingOfImage")
    minDoy = cv2.getTrackbarPos("Min Doy", "settingOfImage")
    maxDoy = cv2.getTrackbarPos("Max Doy", "settingOfImage")
    minVal = cv2.getTrackbarPos("Min Val", "settingOfImage")
    maxVal = cv2.getTrackbarPos("Max Val", "settingOfImage")
    #res = cv2.getTrackbarPos("reset", "settingOfImage")

    upperLimit = np.array([maxTon, maxDoy, maxVal])
    lowerLimit = np.array([minTon, minDoy, minVal])
    mask = cv2.inRange(frameHSV, lowerLimit, upperLimit)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    print(upperLimit, lowerLimit)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # joinedImage = np.hstack([frame, mask, result])

    # joinedWindows = np.hstack([frame, mask, result])
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
