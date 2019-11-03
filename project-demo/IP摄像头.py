# _*_ coding: utf-8 _*_
# @Time     : 2019/9/6 20:44
# @Author   : Ole211
# @Site     : 
# @File     : IP摄像头.py    
# @Software : PyCharm
'''
读取手机摄像头的视频流
1.手机与电脑连接同一个WIFI热点
2. 下载IP摄像APP， 打开IP摄像头服务器
3. 电脑浏览器输入：http://192.168.43.1:8081/
'''
import cv2
cameralAdress = 'http://admin:admin@192.168.43.1:8081/'
cap = cv2.VideoCapture(cameralAdress)
cap1 = cv2.VideoCapture(0)
# cap.set 设定VideoCapture的属性， 指定缓存区的尺寸为1
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while 1:
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    cv2.imshow('frame', frame)
    cv2.imshow('window', frame1)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
