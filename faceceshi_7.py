# -*- coding: cp936 -*-
#��������ͷ�ĵ�ȡ����ʾ
import cv2 as cv
def video_demo():
    capture=cv.VideoCapture(0)
    #����Ϊ��Ƶ�豸��id �����ֻ��һ������ͷ������0����ʾ��Ĭ�ϵ�����ͷ     ����Ĳ���Ҳ��������Ƶ�ļ���·����ֻҪ����Ƶ�ļ��ľ���·��д��ȥ�ͺ�
    while True:  #ֻҪû����ѭ�������ѭ������ÿһ֡ ,waitKey(10)��ʾ���10ms
        ret, frame = capture.read()
        #read������ȡ��Ƶ(����ͷ)��ĳ֡,���ܷ�����������. ��һ��������bool�͵�ret����ֵΪTrue��False��������û�ж���ͼƬ. �ڶ���������frame���ǵ�ǰ��ȡһ֡��ͼƬ
        frame=cv.flip(frame,1)
        #��ת  0:��X�ᷭת(��ֱ��ת)   ����0:��Y�ᷭת(ˮƽ��ת)   С��0:����X�ᷭת������Y�ᷭת���ȼ�����ת180��
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("video",frame)
        pc=cv.waitKey(10)   #����10ms, waitKey�����᷵��-1�����10ms���ڼ��̰���ĳ���������� waitKey�����᷵�ض�Ӧ������ASCII��ֵ��ASCII��ֵһ������0
        if pc>0:
            break
        # if cv.waitKey(10) == ord('z'):  # ��������z�˳����ڣ�����z����رջ�һֱ�ز��� Ҳ�������ó��������� ord()�������ض�Ӧ�ַ���ASCII��ֵ
        #     break
video_demo()
cv.destroyAllWindows()
