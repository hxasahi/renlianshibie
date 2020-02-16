#-*- coding: utf-8 -*-

import cv2
import sys
from PIL import Image

cap = cv2.VideoCapture(0)                
    
classfier = cv2.CascadeClassifier("C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
                                  
color = (0, 255, 0)
        
while cap.isOpened():
    ok, frame = cap.read() 
    if not ok:            
        break
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                 
        
    faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
    if len(faceRects) > 0:            #大于0则检测到人脸                                   
        for faceRect in faceRects:  #单独框出每一张人脸
            x, y, w, h = faceRect        
            cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                        
     #显示图像
    cv2.imshow(window_name, frame)        
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break        
    
cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
    else:
        CatchUsbVideo("识别人脸区域", int(sys.argv[1]))
