import numpy as np
import cv2

imagePath = 'abba.png'
cascPath = 'haarcascade_frontalface_default.xml'


img = cv2.imread(imagePath)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
face_cascade = cv2.CascadeClassifier(cascPath)


faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

print 'faces:', len(faces)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
