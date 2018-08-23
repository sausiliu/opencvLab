# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import cv2

imagepath = r'./face.jpg'
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalcatface.xml')
image = cv2.imread(imagepath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "发现{0}个人脸!".format(len(faces))

for (x, y, w, h) in faces:
    # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    cv2.circle(image, ((x + x + w) / 2, (y + y + h) / 2), w / 2, (0, 255, 0), 2)

cv2.imshow("Find Faces!", image)

cv2.waitKey(0)
