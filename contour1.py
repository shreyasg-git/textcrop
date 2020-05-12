import numpy as np
import cv2

img = cv2.imread('img5.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 0, 2, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cv.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
print("Number of contours = " + str(len(contours)))
'''

x, y, w, h = cv2.boundingRect(thresh)
recta = cv2.rectangle(imgray, (x, y), (x+w, y+h), (0, 125, 0), 2)

'''
rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# hull = cv2.convexHull(contours[1])
# cv2.drawContours(img, contours, -1, (0, 255,255), 1)
# cv2.drawContours(imgray, contours, -1, (0, 255, 0), 1)
# cv2.imshow('Hulls', hull)
for con in contours:
    cv2.drawContours(img, con, -1, (0, 255, 0), 1)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
# cv2.imshow('Recta', recta)
# cv2.imshow('Image GRAY', imgray)

cv2.destroyAllWindows()