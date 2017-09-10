# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2017年09月10日 星期日 13时18分07秒
import fasttext

train_file = '/home/alex/data/hsbianma_page10_sogou_huaxue.fasttext.train.txt'
test_file = '/home/alex/data/hsbianma_page10_sogou_huaxue.fasttext.test.txt'

# 训练
classifier = fasttext.supervised(train_file, 'classify_model')

# 测试
result = classifier.test(test_file)
print('P@1:', result.precision)
print('R@1:', result.recall)
print('Number of examples:', result.nexamples)

def test(test_file):
    pre_len = len('__label__2924')
    with open(test_file) as r:
        total = 0
        topn_num = 5
        topn = [0] * topn_num
        for row in r.readlines():
            row = row.strip()
            kind = row[pre_len-4:pre_len]
            words = row[pre_len+1:]
            res = classifier.predict([words], k=topn_num)
            total += 1
            for i in range(topn_num):
                if kind == res[0][i]:
                    topn[i] += 1

        topn = [i/total for i in topn]
        print("Total: %d   topn:" % total, topn, sum(topn))


test(train_file)
test(test_file)
