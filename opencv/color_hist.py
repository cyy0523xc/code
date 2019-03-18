# -*- coding: utf-8 -*-
#
# 颜色直方图
# python3 color_hist.py /path/to/10.jpg
#
# Author: alex
# Created Time: 2019年03月18日 星期一 11时26分49秒
import cv2
import numpy as np
from matplotlib import pyplot as plt


def gray_hist(img):
    # bins->图像中分为多少格；range->图像中数字范围
    plt.hist(img.ravel(), bins=8, range=[0, 256])
    plt.show()


def gray_hist_cv2(img):
    bins = 16
    histr = cv2.calcHist([img], [0], None, [bins], [0, 256])
    histr = histr/histr.sum()
    histr = [int(i*1000) for i in histr]
    # plt.plot(histr)
    # plt.xlim([0, bins])
    # plt.show()
    return histr


def color_hist(img):
    color = ('b', 'g', 'r')
    bins = 16
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [bins], [0, 256])
        histr = histr/histr.sum()
        histr = [int(i*1000) for i in histr]
        # print(histr)
        plt.plot(histr, color=col)

    plt.xlim([0, bins])
    plt.show()


if __name__ == '__main__':
    import sys
    from imutils.paths import list_images
    rates, rates1, rates2 = [], [], []
    for index, path in enumerate(list_images(sys.argv[1])):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        w = img.shape[1]
        img = img[:, 0:int(w/2)]
        hist = gray_hist_cv2(img)
        hist_rate1 = [hist[i]+hist[i+1]
                     for i in range(len(hist)-1)]
        hist_rate2 = [hist[i]+hist[i+1]+hist[i+2]
                     for i in range(len(hist)-2)]
        rates.append(max(hist))
        rates1.append(max(hist_rate1))
        rates2.append(max(hist_rate2))
        print(index, path, max(hist))
        # img = cv2.imread(path, cv2.IMREAD_COLOR)
        # w = img.shape[1]
        # img = img[:, 0:int(w/2), :]
        # color_hist(img)

    print(min(rates), max(rates), np.average(rates), rates)
    print(min(rates1), max(rates1), np.average(rates1), rates1)
    print(min(rates2), max(rates2), np.average(rates2), rates2)
