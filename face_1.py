# -*- coding: cp936 -*-
import cv2 as cv
src=cv.imread('F:\������\����.jpg')       
cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
cv.imshow('input_image', src)
cv.waitKey(0)
cv.destroyAllWindows()
