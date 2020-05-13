import cv2
from PIL import ImageGrab, Image
import os


img_in = ImageGrab.grabclipboard()
img_in.save('tempsave.png', 'PNG')

img = cv2.imread('tempsave.png')

# resizing using numpy to width = 480
init_sizes = img.shape
print(init_sizes)
new_height = 480*(init_sizes[0] / init_sizes[1])
print(new_height)
img = cv2.resize(img, dsize=(480, int(new_height)), interpolation=cv2.INTER_CUBIC)   # resized

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 4)

contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

xs = []     # x-coordinate of each
ys = []     # y-coordinate of each
xws = []    # (x+w)-coordinate of each
yhs = []    # (y+h)-coordinate of each
margin = 7  # margin to be left

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

# syntax of numpy image slicing - img[y:y+h, x:x+w]
final_image = img[(min(ys) - margin):(max(yhs) + margin), (min(xs) - margin):(max(xws) + margin)]

# resizing using numpy to width = 480
init2_sizes = final_image.shape
print(init2_sizes)
new2_height = 480*(init2_sizes[0] / init2_sizes[1])
print(new2_height)
final_image = cv2.resize(final_image, dsize=(480, int(new2_height)), interpolation=cv2.INTER_CUBIC)   # resized

final_name = input("Enter the output image name")
cv2.imwrite('{}.png'.format(final_name), final_image)
os.remove('tempsave.png')

# cv2.rectangle(img, (min(xs), min(ys)), (max(xws), max(yhs)), (0, 255, 255), 1)
# cv2.imshow("Show", img)
# cv2.imshow("Gray", imgray)
# cv2.waitKey()
# cv2.destroyAllWindows()
