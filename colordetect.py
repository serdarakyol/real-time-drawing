import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 600)
cap.set(4, 400)
cap.set(10, 100)

# selected colors by order green, blue, red. note: created at night [30, 55, 53, 215, 158, 227]x
#After run colorRecognize
#first i have to wrote last 3 number then first three number.
mycolors = [[0, 175, 110, 9, 234, 198], #red
          [90, 101, 0, 122, 255, 140], #blue
          [40, 112, 0, 59, 255, 239], #green
          [14, 181, 0, 62, 255, 255]] #orangex
          #[93, 198, 134, 109, 255, 213]]
#I wrote labels as BGR
colorsLabel = [[24, 24, 238], [238, 24, 24], [52, 238, 24], [8, 180, 253]]
datapoints = []

def detect_color(colors, frame, mycolorsLabel_det):
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    counter = 0
    newPoints = []
    for color in colors:
        upper_limit = np.array(color[3:6])
        lower_limit = np.array(color[0:3])
        mask = cv2.inRange(img_hsv, lower_limit, upper_limit)
        x, y = get_contours(mask)

        #cv2.circle(output, (x, y), 5, mycolorsLabel_det[counter], cv2.FILLED)
        cv2.line(frame, (x, y), (x, y), (255, 0, 0), 5)
        if x != 0 and y != 0:
            newPoints.append([x, y, counter])
        counter += 1
        #cv2.imshow(str(color[0]), mask)
    return newPoints

def get_contours(image): #degistir bunu
    contours, hierarcy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            #cv2.drawContours(output, cnt, -1, (155, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            #print (x, y, w, h)
    return x+w//2, y

def draw(datapoints, mycolorsLabel):
    for point in datapoints:
        print(point[0], point[1])

        #cv2.rectangle(output, (0, int(point[0])), (0, int(point[1])), mycolorsLabel[point[2]], 15, cv2.FILLED)
        cv2.circle(clone, (point[0], point[1]), 8, mycolorsLabel[point[2]], cv2.FILLED)
        #cv2.line(output, point[0], point[1], (255, 0, 0), 10)
        #cv2.circle(output, (point[0], point[1]), 10, (255, 0, 0), 10)
        x = point[0]
        y = point[1]
        print("++++++++", x, y)
        #cv2.line(clone, (x, y), ((x + 1), (y + 1)), (255, 0, 0), 18)

while 1:
    check, frame = cap.read()
    frame = cv2.flip(frame, 1)
    clone = frame.copy()
    getPoints = detect_color(mycolors, clone, colorsLabel)
#
    if len(getPoints) != 0:
        for getpoint in getPoints:
            datapoints.append(getpoint)
    if len(datapoints) != 0:
        draw(datapoints, colorsLabel)

    cv2.imshow("Output", clone)
    cv2.imshow("Original", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
