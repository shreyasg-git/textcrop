import cv2
img = cv2.imread('img1.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 0, 120, 0)
ret, thresh = cv2.threshold(imgray, 127, 255, 4)
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("thresh", thresh)

xs = []
ys = []
xws = []
yhs = []

for c in contours:
    rect = cv2.boundingRect(c)
    # if rect[2] < 100 or rect[3] < 100: continue
    print(cv2.contourArea(c))
    x, y, w, h = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

    xs.append(x)
    ys.append(y)
    xws.append(x+w)
    yhs.append(y+h)

    # cv2.putText(img, 'Moth Detected', (x+w+10,y+h), 0, 0.3, (0, 255, 0))
# print(min(starts))
# print(starts)
# print(max(ends))
# print(ends)

left_up = (min(xs), min(ys))
right_down = (max(xws), max(yhs))

# left_up = (min(ys), min(xs))
# right_down = (max(yhs), max(xws))



cv2.rectangle(img, left_up, right_down, (0, 255, 255), 1)
cv2.imshow("Show", img)
cv2.imshow("Gray", imgray)
cv2.waitKey()
cv2.destroyAllWindows()

"""
Threshold Flags (4th argument)
https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
    0 - cv.THRESH_BINARY  
    1 - cv.THRESH_BINARY_INV
    2 - cv.THRESH_TRUNC
    3 - cv.THRESH_TOZERO
    4 - cv.THRESH_TOZERO_INV == Best for black text on white bg
"""