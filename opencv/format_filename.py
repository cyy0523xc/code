# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年05月05日 星期日 17时16分08秒
import os
import shutil
from imutils.paths import list_images


def move(path):
    for pf in list_images(path):
        f = pf.split('/')[-1]
        new_f = f[0] + ("%05d" % int(f[1:-4])) + f[-4:]
        shutil.move(pf, os.path.join(path, new_f))


move('/home/alex/文档/汕头/data/out20190504')
