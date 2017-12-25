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

neg_fn = '/var/www/data/sentiments/neg.txt'
pos_fn = '/var/www/data/sentiments/pos.txt'
stop_fn = '/var/www/data/sentiments/stopwords.txt'

# 停用词
stop_words = set()
with open(stop_fn, 'r') as f:
    for line in f:
        w = line.strip()
        stop_words.add(w)


## EDA
maxlen = 0
word_freqs = collections.Counter()
num_recs = 0
sentences = []
# process pos
with open(neg_fn, 'r') as f:
    for line in f:
        words = jieba.lcut(line.strip())
        words = [w for w in words if w not in stop_words]
        if len(words) > maxlen:
            maxlen = len(words)
        for word in words:
            if word not in word_freqs:
                word_freqs[word] = 0
            word_freqs[word] += 1
        num_recs += 1
        sentences.append((1, words))

with open(pos_fn, 'r') as f:
    for line in f:
        words = jieba.lcut(line.strip())
        words = [w for w in words if w not in stop_words]
        if len(words) > maxlen:
            maxlen = len(words)
        for word in words:
            if word not in word_freqs:
                word_freqs[word] = 0
            word_freqs[word] += 1
        num_recs += 1
        sentences.append((0, words))

print('max_len ', maxlen)
print('nb_words ', len(word_freqs))

## 准备数据
MAX_FEATURES = int(len(word_freqs)*0.8)
MAX_SENTENCE_LENGTH = maxlen
vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
word2index = {x[0]: i+2 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
word2index["PAD"] = 0
word2index["UNK"] = 1
index2word = {v:k for k, v in word2index.items()}
X = np.empty(num_recs, dtype=list)
y = np.zeros(num_recs)
i=0
for sent in sentences:
    label, words = sent
    seqs = []
    for word in words:
        if word in word2index:
            seqs.append(word2index[word])
        else:
            seqs.append(word2index["UNK"])
    X[i] = seqs
    y[i] = label
    i += 1
X = sequence.pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)

## 数据划分
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

EMBEDDING_SIZE = 128
HIDDEN_LAYER_SIZE = 64
BATCH_SIZE = 32
NUM_EPOCHS = 10

## 网络构建
model = Sequential()
model.add(Embedding(vocab_size, EMBEDDING_SIZE, input_length=MAX_SENTENCE_LENGTH))
model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1))
model.add(Activation("sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

## 网络训练
model.fit(Xtrain, ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS, validation_data=(Xtest, ytest))

## 预测
score, acc = model.evaluate(Xtest, ytest, batch_size=BATCH_SIZE)
print("\nTest score: %.3f, accuracy: %.3f" % (score, acc))
