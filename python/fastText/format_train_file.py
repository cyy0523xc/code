# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2017年09月10日 星期日 13时18分07秒
import csv
import jieba

src = 'news.csv'
train_csv = 'news.train.csv'
test_csv = 'news.test.csv'
train_file = 'fasttext.train.txt'
test_file = 'fasttext.test.txt'


def format_train_file(src, train_file, test_file, train_csv_file, test_csv_file):
    with open(src) as r, \
            open(train_csv_file, 'w') as w_train_csv_f, \
            open(test_csv_file, 'w') as w_test_csv_f, \
            open(train_file, 'w') as w_train, \
            open(test_file, 'w') as w_test:
        i = 0
        csv_r = csv.DictReader(r)
        fieldnames = ('id', 'kind', 'content')
        train_csv = csv.DictWriter(w_train_csv_f, fieldnames=fieldnames)
        test_csv = csv.DictWriter(w_test_csv_f, fieldnames=fieldnames)
        train_csv.writeheader()
        test_csv.writeheader()
        sep_char = ""
        for row in csv_r:
            if not row['id'].isnumeric():
                continue

            row['content'] = row['content'].strip()
            words = jieba.cut(row['content'])
            words = [w for w in words if "\n" not in w]

            i += 1
            if i % 10 == 0:
                w_test.write(sep_char+'__label__' + row['kind'] + ' ' + ' '.join(words))
                test_csv.writerow(row)
            else:
                w_train.write(sep_char+'__label__' + row['kind'] + ' ' + ' '.join(words))
                train_csv.writerow(row)

            sep_char = "\n"


# 格式化训练文件
format_train_file(src, train_file, test_file, train_csv, test_csv)

print("ok")
