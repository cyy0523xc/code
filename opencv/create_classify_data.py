# -*- coding: utf-8 -*-
#
# 提取图像分类特征
# Author: alex
# Created Time: 2019年03月18日 星期一 15时45分23秒
import cv2


def get_features(path):
    """获取图像特征"""
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    color = ('b', 'g', 'r')
    bins = 16
    features = []
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [bins], [0, 256])
        histr = histr/histr.sum()
        histr = [int(i*10000) for i in histr]
        features += histr
        print(histr)

    return features


if __name__ == '__main__':
    import sys
    from imutils.paths import list_images
    for path in list_images(sys.argv[1]):
        print(path)
        get_features(path)
