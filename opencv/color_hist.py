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

is_plot = False


def gray_hist(img):
    # bins->图像中分为多少格；range->图像中数字范围
    plt.hist(img.ravel(), bins=8, range=[0, 256])
    plt.show()


def gray_hist_cv2(img):
    bins = 16
    histr = cv2.calcHist([img], [0], None, [bins], [0, 256])
    histr = histr/histr.sum()
    histr = [int(i*1000) for i in histr]

    if is_plot:
        plt.plot(histr)
        plt.xlim([0, bins])
        plt.show()
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
    rates, rates1, rates2, rates_sum = [], [], [], []
    white_rate = []
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
        rates_sum.append(sum(hist[6:12]))
        print(index, path, max(hist), hist.index(max(hist)))

        cv2.imshow('gray', img)
        cv2.waitKey(0)
        # gray = cv2.bitwise_not(img)
        # cv2.imshow('bitwise', bitwise)
        # print(bitwise[0:10, 0:10])
        # cv2.waitKey(0)

        # 二值化
        # ret, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        # cv2.imshow('threshold', th1)
        # cv2.waitKey(0)

        # 自适应阈值：
        # 根据图像上的每一个小区域计算与其对应的阈值。
        # 因此在同一幅图像上的不同区域采用的是不同的阈值，
        # 从而使我们能在亮度不同的情况下得到更好的结果。
        # th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    # cv2.THRESH_BINARY, 3, 5)
        # cv2.imshow('threshold2', th2)
        # cv2.waitKey(0)

        th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 3, 6)
        r = th3.sum() / (255*th3.shape[0]*th3.shape[1])
        white_rate.append(r)
        print(th3.shape, r)
        cv2.imshow('threshold3', th3)
        cv2.waitKey(0)

        # 检测直线
        # 第4个参数就是阈值，阈值越大，检测精度越高
        img = cv2.imread(path)
        img = cv2.Canny(img, 50, 200, apertureSize=3)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        minLineLength = 0
        maxLineGap = 0
        th3 = img
        lines = cv2.HoughLinesP(th3, 1, np.pi/180, 100, minLineLength, maxLineGap)
        if lines is not None:
            print("===>", len(lines))
        else:
            lines = cv2.HoughLinesP(th3, 1, np.pi/180, 50, minLineLength, maxLineGap)
            if lines is not None:
                print("--->", len(lines))
            else:
                lines = cv2.HoughLinesP(th3, 1, np.pi/180, 20, minLineLength, maxLineGap)
                if lines is not None:
                    print(">>>>", len(lines))
                else:
                    print("!!!")

        # 显示直线
        if lines is not None:
            for x1, y1, x2, y2 in lines[0]:
                cv2.line(th3, (x1, y1), (x2, y2), (55, 100, 195),
                         1, cv2.LINE_AA)

        cv2.imshow('lines', th3)
        cv2.waitKey(0)

        # 移除噪声点
        # th4 = cv2.fastNlMeansDenoising(th3,10,10,7,21)
        # cv2.imshow('threshold4', th4)
        # cv2.waitKey(0)

        # img = cv2.GaussianBlur(img, (3, 3), 0)
        # canny = cv2.Canny(img, 50, 150)
        # cv2.imshow('canny', img)
        # cv2.waitKey(0)

    print(min(rates), max(rates), np.average(rates), "\n", rates)
    print(min(rates1), max(rates1), np.average(rates1), "\n", rates1)
    print(min(rates2), max(rates2), np.average(rates2), "\n", rates2)
    print(min(rates_sum), max(rates_sum), np.average(rates_sum), "\n", rates_sum)
    print(min(white_rate), max(white_rate), np.average(white_rate), "\n", white_rate)
    sys.exit(0)

    for index, path in enumerate(list_images(sys.argv[1])):
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        w = img.shape[1]
        img = img[:, 0:int(w/2), :]
        color_hist(img)
