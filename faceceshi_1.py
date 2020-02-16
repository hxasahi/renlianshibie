# -*- coding: cp936 -*-
#电脑摄像头的调取和显示
import cv2 as cv
def video_demo():
    capture=cv.VideoCapture(0)
    #参数为视频设备的id ，如果只有一个摄像头可以填0，表示打开默认的摄像头     这里的参数也可以是视频文件名路径，只要把视频文件的具体路径写进去就好
    while True:  #只要没跳出循环，则会循环播放每一帧 ,waitKey(10)表示间隔10ms
        ret, frame = capture.read()
        #read函数读取视频(摄像头)的某帧,它能返回两个参数. 第一个参数是bool型的ret，其值为True或False，代表有没有读到图片. 第二个参数是frame，是当前截取一帧的图片
        frame=cv.flip(frame,1)
        #翻转  0:沿X轴翻转(垂直翻转)   大于0:沿Y轴翻转(水平翻转)   小于0:先沿X轴翻转，再沿Y轴翻转，等价于旋转180°
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("video",frame)
        pc=cv.waitKey(10)   #超过10ms, waitKey函数会返回-1，如果10ms内在键盘按了某个按键，则 waitKey函数会返回对应按键的ASCII码值，ASCII码值一定大于0
        if pc>0:
            break
        # if cv.waitKey(10) == ord('z'):  # 键盘输入z退出窗口，不按z点击关闭会一直关不掉 也可以设置成其他键。 ord()函数返回对应字符的ASCII数值
        #     break
video_demo()
cv.destroyAllWindows()
