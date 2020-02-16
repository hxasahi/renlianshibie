# -*- coding: cp936 -*-
import cv2 as cv
src=cv.imread('F:\人脸库\韩旭.jpg')       
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
cv.waitKey(0)
cv.destroyAllWindows()
