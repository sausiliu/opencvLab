import numpy as np
import cv2 as cv

img_path="./data/test/red_retangle.png"
imgCp_path="./data/test/red_retangle_copy.png"
# img_path = "./data/test/red_retangle_cube.jpg"

image = cv.imread(img_path)
image_cp = cv.imread(imgCp_path)
# image_against = ~image

lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])

image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# image_hsv[...]=0
mask = cv.inRange(image_hsv, lower_red, upper_red)

lower_red = np.array([170, 70, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv.inRange(image_hsv, lower_red, upper_red)
maskAll = mask | mask2

and_img = cv.bitwise_and(image, image_cp, mask=maskAll)
and_cp_img = cv.bitwise_and(image, image_cp, mask=maskAll)

cv.imshow("mask", maskAll)
cv.imshow("and", and_cp_img)
cv.imshow("mask and", np.hstack([image, and_img]))

cv.waitKey(0)

