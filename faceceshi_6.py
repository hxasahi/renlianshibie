# -*- coding: cp936 -*-

import cv2

import numpy as np

def video_demo():

    capture=cv.VideoCapture(0)

    classfier = cv.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    
    while True:  
        ret, frame = capture.read()
        
        frame=cv.flip(frame,1)
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        '''faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))

        if len(faceRects) > 0:            #大于0则检测到人脸                                   

            for faceRect in faceRects:  #单独框出每一张人脸

                x, y, w, h = faceRect        

                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                        
'''
        cv.imshow("video",gray)

        pc=cv.waitKey(10)  

        if pc>0:
            break
        
video_demo()

cv.destroyAllWindows()
