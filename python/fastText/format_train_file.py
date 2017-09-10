# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2017年09月10日 星期日 13时18分07秒
import csv
import jieba

src = '/home/alex/data/hsbianma_page10_sogou_huaxue.csv'
train_file = '/home/alex/data/hsbianma_page10_sogou_huaxue.fasttext.train.txt'
test_file = '/home/alex/data/hsbianma_page10_sogou_huaxue.fasttext.test.txt'


def format_train_file(src, train_file, test_file):
    with open(src) as r, open(train_file, 'w') as w_train, open(test_file, 'w') as w_test:
        csv_r = csv.DictReader(r, fieldnames=('kind', 'content'))
        i = 0
        words_set = set()
        for row in csv_r:
            row['content'] = row['content'].strip()
            if "\n" in row['content']:
                continue

            words = jieba.cut(row['content'])
            if (row['kind'], row['content']) in words_set:
                continue
            words_set.add((row['kind'], row['content']))

            i += 1
            if i % 10 == 0:
                w_test.write('__label__' + row['kind'][:4] + ' ' + ' '.join(words) + "\n")
            else:
                w_train.write('__label__' + row['kind'][:4] + ' ' + ' '.join(words) + "\n")


# 格式化训练文件
format_train_file(src, train_file, test_file)

print("ok")
