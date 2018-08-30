import numpy as np
import cv2 as cv

img_path = './data/images/demo1.png'

image = cv.imread(img_path)
image_bilateral = cv.bilateralFilter(image, 9, 75, 75)
image_denoising = cv.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
cv.namedWindow("origin->bilateral->denoising", cv.WINDOW_NORMAL)
cv.imshow("origin->bilateral->denoising", np.hstack([image, image_bilateral, image_denoising]))


hsv_img = cv.cvtColor(image_denoising, cv.COLOR_BGR2HSV)   # HSV imageage

COLOR_MIN = np.array([20, 100, 100], np.uint8)  # HSV color code lower and upper bounds
COLOR_MAX = np.array([30, 255, 255], np.uint8)  # color yellow

img_mask = cv.inRange(hsv_img, COLOR_MIN, COLOR_MAX)  # Thresholding image
cv.imshow("freame_threshed", img_mask)

# img_ray = frame_threshed
# ret, thresh = cv.threshold(frame_threshed, 127, 255, 0)
# cv.imshow("threshold", thresh)

img2, contours, hierarchy = cv.findContours(img_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(type(contours))


for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    print("x: {0}, y: {1}".format(x, y))
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Show", image)
cv.imwrite("extracted.jpg", image)
cv.waitKey()
cv.destroyAllWindows()
