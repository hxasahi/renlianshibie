# -*- coding: cp936 -*-
import cv2
import numpy as np
#First we need to load the required XML classifiers. Then load our input image (or video) in grayscale mode
face_cascade=cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")#������ubuntuϵͳ���Ѿ�ѵ���õķ�����
eye_cascade=cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data//haarcascade_eye.xml")
cap=cv2.VideoCapture(0)#������ͷ
#open camera
while(1):
    ret,frame=cap.read()
#get frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#�Ҷ�ת��
    faces=face_cascade.detectMultiScale(gray,1.3,5)   
#����  
#Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h). Once we get these locations, we can create a ROI ������Ȥ������for the face and apply eye detection on this ROI (since eyes are always on the face !!! ).
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)#frameͼ��������꣬�յ����꣨��������x+w,y+h,��Ϊw,h�ֱ��������ĳ�����ɫ���߿�
        cv2.putText(i,'face',(w/2+x,y-h/5),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)#���face�ı�ǩ
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)#����۾�
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)#ͬ�ϻ������Ŀ�
            cv2.putText(i,'eye',(ex+x,ey+y),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)#����۾��ı�ǩ
    if cv2.waitKey(1)&0xFF==ord('q')or ret==False:
        break
    cv2.imshow("xiaorun",frame)
cap.release()
cv2.destroyAllwindows()
