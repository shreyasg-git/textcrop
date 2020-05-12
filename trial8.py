import numpy as np
import cv2

img = cv2.imread('img1.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval = cv2.boundingRect(imgray)

bond = cv2.drawContours(img, retval, 0, 255)
cv2.imshow('Image', retval)
cv2.imshow('Bond', bond)
cv2.waitKey(0)
cv2.destroyAllWindows()