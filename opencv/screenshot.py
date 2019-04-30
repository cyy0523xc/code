# -*- coding: utf-8 -*-
#
# 截图
# Author: alex
# Created Time: 2019年04月30日 星期二 14时11分38秒
import os
import cv2


def screenshot(path, output_path, fn_prefix='img_', duration=1000):
    """
    Args:
        path: 视频路径
        output_path: 图片保存路径
        fn_prefix: 图片名称前缀
        duration: 保存时间间隔
    """
    vc = cv2.VideoCapture(path)
    if vc.isOpened() is False:
        raise Exception('视频文件打开失败')

    c = 0
    fps = int(vc.get(cv2.CAP_PROP_FPS))
    mod = max(int(fps * duration / 1000), 4)  # 计算每多少帧保存一个截图
    while True:
        rval, frame = vc.read()
        if rval is False:
            break
        if c % mod == 0:
            fn = '%s%08d.jpg' % (fn_prefix, c)
            cv2.imwrite(os.path.join(output_path, fn), frame)

        c += 1
        cv2.waitKey(1)

    vc.release()


if __name__ == '__main__':
    import fire
    fire.Fire(screenshot)
