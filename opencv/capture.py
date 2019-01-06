# -*- coding: utf-8 -*-
#
# 录制视频
# Author: alex
# Created Time: 2019年01月06日 星期日 10时36分05秒
import cv2

cap = cv2.VideoCapture(0)
# outfile = 'output.mp4'
# fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
outfile = 'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 第三个参数则是镜头快慢的，20为正常，小于二十为慢镜头
out = cv2.VideoWriter(outfile, fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret is False:
        break

    frame = cv2.flip(frame, 1)
    out.write(frame)
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
