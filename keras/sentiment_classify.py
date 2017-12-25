# -*- coding: utf-8 -*-
#
# 使用LSTM进行情感分类
# Author: alex
# Created Time: 2017年12月24日 星期日 17时23分22秒
import jieba
import collections
import numpy as np

from keras.layers.core import Activation, Dense
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.preprocessing import sequence
from sklearn.model_selection import train_test_split

# 语料库及停用词
neg_fn = '/var/www/data/sentiments/neg.txt'
pos_fn = '/var/www/data/sentiments/pos.txt'
stop_fn = '/var/www/data/sentiments/stopwords.txt'

# 停用词
stop_words = set()
with open(stop_fn, 'r') as f:
    for line in f:
        w = line.strip()
        stop_words.add(w)

# 处理样本文本
maxlen = 0
word_freqs = collections.Counter()
distribution = collections.Counter()
num_recs = 0
sentences = []
with open(neg_fn, 'r') as f:
    for line in f:
        words = jieba.lcut(line.strip())
        words = [w for w in words if w not in stop_words]
        lw = len(words)
        if lw > maxlen:
            maxlen = lw
        for word in words:
            word_freqs[word] += 1
        num_recs += 1
        sentences.append((1, words))
        distribution[lw//100] += 1

with open(pos_fn, 'r') as f:
    for line in f:
        words = jieba.lcut(line.strip())
        words = [w for w in words if w not in stop_words]
        lw = len(words)
        if lw > maxlen:
            maxlen = lw
        for word in words:
            word_freqs[word] += 1
        num_recs += 1
        sentences.append((0, words))
        distribution[lw//100] += 1

print('单个样本最大长度： ', maxlen)
print('单个样本最大长度： ', maxlen)
print('去重后的有效词的数量： ', len(word_freqs))
print('样本有效长度分布：', distribution)

# 只保留词频大于1的词
print('只保留词频大于1的')
maxlen = 0
num_recs = 0
distribution = collections.Counter()
word_freqs = {k:v for k, v in enumerate(word_freqs) if v > 1}
for i, x in enumerate(sentences):
    sentences[i][1] = [w for w in x[1] if w in word_freqs]
    lw = len(sentences[i][1])
    distribution[lw//100] += 1
    if lw > maxlen:
        maxlen = lw

print('单个样本最大长度： ', maxlen)
print('单个样本最大长度： ', maxlen)
print('去重后的有效词的数量： ', len(word_freqs))
print('样本有效长度分布：', distribution)

# 准备数据
# 最大的特征数量
# 实际预测的时候，可能有些特征并没有在样本里体现，这时可以用UNK来替代
MAX_FEATURES = len(word_freqs)
# 根据样本的最大长度，可以统一文本向量长度
MAX_SENTENCE_LENGTH = maxlen

# 将文本转化为向量下标
vocab_size = MAX_FEATURES + 2
word2index = {x[0]: i+2 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
word2index["PAD"] = 0
word2index["UNK"] = 1
index2word = {v:k for k, v in word2index.items()}
X = np.empty(num_recs, dtype=list)
y = np.zeros(num_recs)
i = 0
for sent in sentences:
    label, words = sent
    seqs = [word2index[w] if w in word2index else word2index["UNK"] for w in words]
    X[i] = seqs
    y[i] = label
    i += 1
X = sequence.pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)

# 数据划分
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# 模型配置参数
EMBEDDING_SIZE = 128
HIDDEN_LAYER_SIZE = 64
BATCH_SIZE = 32
NUM_EPOCHS = 5

# 网络构建
model = Sequential()
model.add(Embedding(vocab_size, EMBEDDING_SIZE, input_length=MAX_SENTENCE_LENGTH))
model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1))
model.add(Activation("sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# 网络训练
model.fit(Xtrain, ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS, validation_data=(Xtest, ytest))

# 保存模型
model.save_weights('sentiment.keras.model.h5', overwrite=True)
with open('sentiment.keras.model.json', 'w') as f:
    model_json = model.to_json()
    f.write(model_json)

# 预测
score, acc = model.evaluate(Xtest, ytest, batch_size=BATCH_SIZE)
print("\nTest score: %.3f, accuracy: %.3f" % (score, acc))
