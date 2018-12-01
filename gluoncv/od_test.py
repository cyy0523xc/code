# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年12月01日 星期六 18时26分51秒
from matplotlib import pyplot as plt
from gluoncv import model_zoo, data, utils

net = model_zoo.get_model('faster_rcnn_resnet50_v1b_voc', pretrained=True)


def detect(path):
    x, orig_img = data.transforms.presets.rcnn.load_test(path)
    print(x.shape)
    print(net.classes)
    class_names = net.classes
    box_ids, scores, bboxes = net(x)
    utils.viz.plot_bbox(orig_img, bboxes[0], scores[0], box_ids[0],
                        class_names=class_names)
    plt.show()


if __name__ == '__main__':
    import sys
    detect(sys.argv[1])
