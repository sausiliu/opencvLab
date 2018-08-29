import numpy as np
import cv2
from cv2 import *

img_path = './data/images/demo1.png'

image = cv2.imread(img_path)
image = cv2.bilateralFilter(image, 9, 75, 75)
image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)   # HSV imageage

COLOR_MIN = np.array([20, 100, 100], np.uint8)  # HSV color code lower and upper bounds
COLOR_MAX = np.array([30, 255, 255], np.uint8)  # color yellow

frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)     # Thresholding image

img_ray = frame_threshed

ret, thresh = cv2.threshold(frame_threshed, 127, 255, 0)
img2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(type(contours))


for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    print(x)
    print(y)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Show", image)
cv2.imwrite("extracted.jpg", image)
cv2.waitKey()
cv2.destroyAllWindows()
