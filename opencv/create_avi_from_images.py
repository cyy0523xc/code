# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年05月11日 星期六 16时55分25秒
import cv2
from imutils.paths import list_images


def create(path):
    images = list(list_images(path))
    outfile = '/tmp/out.avi'
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None
    fps = 3
    print(len(images))
    for img in sorted(images):
        image = cv2.imread(img)
        if out is None:
            h, w = image.shape[:2]
            print(h, w)
            out = cv2.VideoWriter(outfile, fourcc, fps, (w, h))

        out.write(image)


if __name__ == "__main__":
    import sys
    create(sys.argv[1])
