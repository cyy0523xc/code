# -*- coding: utf-8 -*-
#
# 将图片自动进行矫正
# Author: alex
# Created Time: 2018年12月07日 星期五 16时46分49秒
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image file")
ap.add_argument("-o", "--out-image", default='',
                help="path to save image file")
args = vars(ap.parse_args())
print(args)

# load the image from disk
image = cv2.imread(args["image"])

# convert the image to grayscale and flip the foreground
# and background to ensure foreground is now "white" and
# the background is "black"
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

# threshold the image, setting all foreground pixels to
# 255 and all background pixels to 0
thresh = cv2.threshold(gray, 0, 255,
                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# grab the (x, y) coordinates of all pixel values that
# are greater than zero, then use these coordinates to
# compute a rotated bounding box that contains all
# coordinates
coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]

# the `cv2.minAreaRect` function returns values in the
# range [-90, 0); as the rectangle rotates clockwise the
# returned angle trends to 0 -- in this special case we
# need to add 90 degrees to the angle
if angle < -45:
    angle = -(90 + angle)
else:
    # otherwise, just take the inverse of the angle to make
    # it positive
    angle = -angle

# rotate the image to deskew it
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h),
                         flags=cv2.INTER_CUBIC,
                         borderMode=cv2.BORDER_REPLICATE)

# draw the correction angle on the image so we can validate it
"""
cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
"""

# show the output image
print("[INFO] angle: {:.3f}".format(angle))
if len(args['out_image']):
    # rotated = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(args['out_image'], rotated)

cv2.imshow("Input", image)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
