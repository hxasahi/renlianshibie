import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_eye.xml")
i = cv2.imread('d.jpg')
print (i.shape)

gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (5,5),
)

l=len(faces)
print (l)
for (x,y,w,h) in faces:
    cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(i,'face',(w//2+x,y-h//5),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = i[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

cv2.putText(i,"face count",(20,20),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
cv2.putText(i,str(l),(230,20),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)

'''#cv2.putText(i,"eyes count",(20,60),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
print (i.shape)	#cv2.putText(i,str(r),(230,60),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
'''
cv2.imshow("img",i)

cv2.waitKey(0)
