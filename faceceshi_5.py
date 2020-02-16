# -*- coding: cp936 -*-
import cv2
import numpy as np
#First we need to load the required XML classifiers. Then load our input image (or video) in grayscale mode
face_cascade=cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")#这是我ubuntu系统里已经训练好的分类器
eye_cascade=cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data//haarcascade_eye.xml")
cap=cv2.VideoCapture(0)#打开摄像头
#open camera
while(1):
    ret,frame=cap.read()
#get frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#灰度转换
    faces=face_cascade.detectMultiScale(gray,1.3,5)   
#画框  
#Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h). Once we get these locations, we can create a ROI （感兴趣的区域）for the face and apply eye detection on this ROI (since eyes are always on the face !!! ).
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)#frame图像，起点坐标，终点坐标（在这里是x+w,y+h,因为w,h分别是人脸的长宽）颜色，线宽）
        cv2.putText(i,'face',(w/2+x,y-h/5),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)#标出face的标签
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)#检测眼睛
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)#同上画出脸的框
            cv2.putText(i,'eye',(ex+x,ey+y),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)#标出眼睛的标签
    if cv2.waitKey(1)&0xFF==ord('q')or ret==False:
        break
    cv2.imshow("xiaorun",frame)
cap.release()
cv2.destroyAllwindows()
