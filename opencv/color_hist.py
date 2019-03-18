# -*- coding: utf-8 -*-
#
# 颜色直方图
# python3 color_hist.py /path/to/10.jpg
#
# Author: alex
# Created Time: 2019年03月18日 星期一 11时26分49秒
import cv2
from matplotlib import pyplot as plt


def gray_hist(img):
    # bins->图像中分为多少格；range->图像中数字范围
    plt.hist(img.ravel(), bins=8, range=[0, 256])
    plt.show()


def color_hist(img):
    color = ('b', 'g', 'r')
    bins = 16
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [bins], [0, 256])
        histr = histr/histr.sum()
        histr = [int(i*10000) for i in histr]
        # print(histr)
        plt.plot(histr, color=col)

    plt.xlim([0, bins])
    plt.show()


if __name__ == '__main__':
    import sys
    from imutils.paths import list_images
    for path in list_images(sys.argv[1]):
        print(path)
        # img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        # gray_hist(img)
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        color_hist(img)
