# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2017年09月10日 星期日 13时18分07秒
import csv
import jieba
import fasttext

train_file = 'fasttext.train.txt'
test_file = 'fasttext.test.txt'

# 训练
classifier = fasttext.supervised(train_file, 'classify_model',
                                 lr=1.0,
                                 epoch=30,
                                 #word_ngrams=2
                                 loss='hs'
                                 )

# 测试
result = classifier.test(train_file)
print('P@1:', result.precision)
print('R@1:', result.recall)
print('Number of examples:', result.nexamples)

# 测试
result = classifier.test(test_file)
print('P@1:', result.precision)
print('R@1:', result.recall)
print('Number of examples:', result.nexamples)


def test(test_file):
    with open(test_file) as r:
        total = 0
        topn_num = 1
        topn = [0] * topn_num
        cr = csv.DictReader(r)
        kinds = set()
        for row in cr:
            words = jieba.cut(row['content'])
            words = [w for w in words if "\n" not in w]
            if len(words) < 1:
                continue

            res = classifier.predict([" ".join(words)], k=topn_num)
            kinds.add(row['kind'])
            total += 1
            for i in range(topn_num):
                if row['kind'] == res[0][i]:
                    topn[i] += 1

        topn = [i/total for i in topn]
        print("Total: %d   topn:" % total, topn, sum(topn))
        print(kinds)


train_file = 'news.train.csv'
test_file = 'news.test.csv'
test(train_file)
test(test_file)
