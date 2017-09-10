# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2017年09月10日 星期日 13时18分07秒
import csv
import jieba
import fasttext

train_file = '/home/alex/data/hsbianma_page10_sogou_huaxue.csv'
train_file_output = '/home/alex/data/hsbianma_page10_sogou_huaxue.fasttext.txt'


def format_train_file(csv_file, train_file):
    with open(csv_file) as r, open(train_file, 'w') as w:
        csv_r = csv.DictReader(r, fieldnames=('kind', 'content'))
        for row in csv_r:
            row['content'] = row['content'].strip()
            if "\n" in row['content']:
                continue

            words = jieba.cut(row['content'])
            w.write('__label__' + row['kind'][:4] + ' ' + ' '.join(words) + "\n")


# 格式化训练文件
format_train_file(train_file, train_file_output)

# 训练
classifier = fasttext.supervised(train_file_output, 'classify_model')

# 测试
result = classifier.test(train_file_output)
print('P@1:', result.precision)
print('R@1:', result.recall)
print('Number of examples:', result.nexamples)

# 预测
classifier.predict([' '.join(jieba.cut("锦纶天丝面料"))], k=3)
