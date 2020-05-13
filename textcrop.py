import cv2

img = cv2.imread('img7.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 4)

contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow("thresh", thresh)

xs = []     # x-coordinate of each
ys = []     # y-coordinate of each
xws = []    # (x+w)-coordinate of each
yhs = []    # (y+h)-coordinate of each
margin = 2  # margin to be left

for c in contours:

    rect = cv2.boundingRect(c)
    x, y, w, h = rect
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1) # individual bounding rectangles

    xs.append(x)
    ys.append(y)
    xws.append(x+w)
    yhs.append(y+h)

    # cv2.putText(img, 'Moth Detected', (x+w+10,y+h), 0, 0.3, (0, 255, 0))

# print(min(starts))
# print(starts)
# print(max(ends))
# print(ends)

# left_up = (min(ys), min(xs))
# right_down = (max(yhs), max(xws))

# syntax of numpy image slicing - img[y:y+h, x:x+w]
final_image = img[(min(ys) - margin):(max(yhs) + margin), (min(xs) - margin):(max(xws) + margin)]

final_name = input("Enter the output image name")
cv2.imwrite('{}.png'.format(final_name), final_image)

cv2.rectangle(img, (min(xs), min(ys)), (max(xws), max(yhs)), (0, 255, 255), 1)
cv2.imshow("Show", img)
# cv2.imshow("Gray", imgray)
cv2.waitKey()
cv2.destroyAllWindows()
