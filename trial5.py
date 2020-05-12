import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # lower_blue = np.array([38, 86, 0])
    # upper_blue = np.array([121, 255, 255])
    # mask = cv.inRange(hsv, lower_blue, upper_blue)

    ret, thresh = cv.threshold(hsv, 0, 2, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    # _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv.imshow("Video", frame)
    cv.imshow("Mask", mask)
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()