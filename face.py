# coding:utf-8
# import sys
import cv2 as cv

imagePath = r'./face.jpg'
haarCascadePath = r'./data/haarcascade/haarcascade_frontalface_default.xml'

face_cascade = cv.CascadeClassifier(haarCascadePath)
image = cv.imread(imagePath)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5),
    flags=cv.CASCADE_SCALE_IMAGE
)
# flags=cv.CV_HAAR_SCALE_IMAGE

print("发现{0}个人脸!".format(len(faces)))

for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w, y+w), (0, 255, 0), 2)
    # cv.circle(image, ((x+x+w)/2, (y+y+h)/2), w/2, (0,255,0), 2)

cv.imshow("Find Faces!", image)

cv.waitKey(0)
