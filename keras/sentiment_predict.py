# -*- coding: utf-8 -*-
#
# 使用已经训练好的模型进行情感分类
# Author: alex
# Created Time: 2017年12月25日 星期一 11时41分34秒
import jieba
from keras.models import model_from_json

model_h5_fn = 'sentiment.keras.model.h5'
model_json_fn = 'sentiment.keras.model.json'

sentences = [
    "这本书的质量很差",
    "这个手机看起来比较一般，但是用起来还是很不错的"
]

stop_fn = '/var/www/data/sentiments/stopwords.txt'

# 停用词
stop_words = set()
with open(stop_fn, 'r') as f:
    for line in f:
        w = line.strip()
        stop_words.add(w)

for s in sentences:
    words = jieba.lcut(s)
    words = [w for w in words if w not in stop_words]
    print("{}: {}")


model = model_from_json(open(model_json_fn).read())
model.load_weights(model_h5_fn)

