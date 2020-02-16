# -*- coding: cp936 -*-

import cv2

import cv2 as cv

import numpy as np

face_cascade=cv.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
eye_cascade=cv.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_eye.xml")

capture=cv.VideoCapture(0)

classfier = cv.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    
while True:  
    ret, frame = capture.read()
    
    frame=cv.flip(frame,1)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (5,5),
    )

    l=len(faces)
    #print (l)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv.putText(frame,'face',(w//2+x,y-h//5),cv.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

    cv.putText(frame,"face count",(20,20),cv.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
    cv.putText(frame,str(l),(230,20),cv.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)

    cv.startWindowThread()

    cv.imshow("video",frame)

    pc=cv.waitKey(10)  

    if pc>0:
        cv.destroyAllWindows()
        break

