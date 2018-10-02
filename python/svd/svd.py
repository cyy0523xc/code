# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年10月02日 星期二 20时14分08秒
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
from matplotlib.font_manager import FontProperties
from numpy import linalg as la

# 中文字体文件
myfont = FontProperties(fname='/usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/SIMHEI.TTF')


def gen_words(sents: list) -> tuple:
    """生成词典"""
    words = set(sents[0])
    if len(sents) > 1:
        for i in range(1, len(sents)):
            words = words.union(set(sents[i]))

    return tuple(words)


def gen_matrix(sents, words):
    """生成矩阵"""
    # 建立倒排索引
    index = {w: set() for w in words}
    for i in range(len(sents)):
        for w in sents[i]:
            index[w].add(i)

    n = len(words)
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                m[i, j] = 0
                continue
            wi = words[i]
            wj = words[j]
            vi = index[wi]
            m[i, j] = len(vi.intersection(index[wj]))

    return m


def svd_show(words, matrix):
    # svd分解
    U, _, _ = la.svd(matrix, full_matrices=False)

    # 将特征向量归一化
    #U_tmp = U[:, 0:2]
    #x_min, x_max = U_tmp.min(0), U_tmp.max(0)
    #U_norm = (U_tmp - x_min) / (x_max - x_min)  # 归一化
    #print(U_norm)

    # t-SNE降维并归一化
    tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
    X_tsne = tsne.fit_transform(U)
    x_min, x_max = X_tsne.min(0), X_tsne.max(0)
    X_norm = (X_tsne - x_min) / (x_max - x_min)  # 归一化
    print('t-SNE')
    print(X_norm)

    plt.axis([0, 1, 0, 1])
    for i in range(len(words)):
        #plt.text(U_norm[i, 0], U_norm[i, 1], words[i], fontproperties=myfont)
        plt.text(X_norm[i, 0], X_norm[i, 1], words[i], fontproperties=myfont)

    plt.show()


if __name__ == '__main__':
    sents = [
        '外观 很 漂亮',
        '外观 好看 用着 好',
        '手机 非常 漂亮',
        '外观 还是 比较 漂亮 的',
        '手机 外观 非常 漂亮',
        '外观 也 非常 好看',
    ]
    sents = [
        'I like deep learning .',
        'I like NLP .',
        'I enjoy flying .',
    ]
    sents = [s.split() for s in sents]
    words = gen_words(sents)
    print('words:', words)
    matrix = gen_matrix(sents, words)
    print(matrix)
    svd_show(words, matrix)
