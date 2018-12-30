# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年12月30日 星期日 11时38分51秒
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
    _, frame = cap.read()

    fgmask = fgbg.apply(frame)
    cv2.imshow('org', frame)
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
