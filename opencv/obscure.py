# -*- coding: utf-8 -*-
#
# 判断图片的模糊程度
# Author: alex
# Created Time: 2019年01月26日 星期六 21时21分29秒
import os
import sys
import cv2


if __name__ == '__main__':
    shape = None
    path = sys.argv[1]
    for f in sorted(os.listdir(path)):
        image = cv2.imread(os.path.join(path, f))
        if shape is None:
            shape = (image.shape[0], image.shape[1])
        else:
            image = cv2.resize(image, shape, interpolation=cv2.INTER_CUBIC)

        img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
        print(f, imageVar)
