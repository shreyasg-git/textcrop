import numpy as np
import cv2

img = cv2.imread('img5.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([125, 125, 125])
upper_blue = np.array([200, 200, 200])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imshow("Video", img)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows(0)