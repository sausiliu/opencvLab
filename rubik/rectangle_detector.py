# refer the OpenCV example:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

import cv2 as cv
import math
#import numpy as np

img_path = './data/images/demo1.png'
#img_path = './data/images/demo4.png'


img_orig = cv.imread(img_path)
# gray
image_bilateral = cv.bilateralFilter(img_orig, 9, 75, 75)
# image_denoising = cv.fastNlMeansDenoisingColored(image_bilateral, None, 10, 10, 7, 21)

image = cv.cvtColor(image_bilateral, cv.COLOR_BGR2GRAY)
cv.namedWindow("gray image", cv.WINDOW_NORMAL)
cv.imshow("gray image", image)

# Gaussian Filter
# image = cv.GaussianBlur(image, (5, 5), 80)
# cv.namedWindow("Gaussian Blurred", cv.WINDOW_NORMAL)
# cv.imshow("Gaussian Blurred", image)

# Canny Filter

image = cv.Canny(image, 20, 40, 3)
cv.namedWindow("Edge", cv.WINDOW_NORMAL)
# 圆滑边缘信息
# image = cv.GaussianBlur(image, (3, 3), 2)
# image = cv.bilateralFilter(image, 9, 75, 75)

cv.imshow("Edge", image)

img = img_orig
img2, contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0, 0, 255), 3)
cv.namedWindow("Contours", cv.WINDOW_NORMAL)
cv.imshow("Contours", img)

print("Contours length:")
print(len(contours))

for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    if w < 20 or h < 20:
        continue
    # print("x:{0}, y:{1} , w:{2}, h: {3}".format(x, y, w, h))
    #cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    approx = cv.approxPolyDP(cnt, 100, True)
    #cv.polylines(img, [approx], True, (0, 0, 255), 2)
    # if approx.size == 4 \
    #         and math.fabs(cv.contourArea(cnt)) > 5 \
    #         and cv.isContourConvex(cnt):
    print(approx.size)
    if approx.size == 4:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.namedWindow("Output", cv.WINDOW_NORMAL)
cv.imshow("Output", img)

cv.waitKey()
cv.destroyAllWindows()

