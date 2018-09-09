# -*- coding: utf-8 -*-
#
# lstm用于情感分类（Python3）
# Author: alex
# Created Time: 2018年07月06日 星期五 15时42分47秒
from keras_text.data import Dataset
from keras_text.models import SentenceModelFactory
from keras_text.models import YoonKimCNN, AttentionRNN, StackedRNN, AveragingEncoder

corpus_path = '/var/www/src/github.com/nlp/ChineseNlpCorpus/format_datasets/'


def tokenizer(text):
    """"""


def lstm_train(pos_filename, neg_filename, epoch=20, window_size=10, batch_size=32,
               input_length=100, vocab_dim=100, maxlen=100):
    """训练
    Args:
        pos_filename: 正面文件名
        neg_filename: 负面文件名
    """
    X, y = load_corpus(corpus_path+pos_filename, corpus_path+neg_filename)
    ds = Dataset(X, y, tokenizer=tokenizer)
    ds.update_test_indices(test_size=0.1)

    # Pad sentences to 500 and words to 200.
    factory = SentenceModelFactory(10, tokenizer.token_index, max_sents=500, max_tokens=500, embedding_type='glove.6B.100d')
    word_encoder_model = AttentionRNN()
    sentence_encoder_model = AttentionRNN()

    # Allows you to compose arbitrary word encoders followed by sentence encoder.
    model = factory.build_model(word_encoder_model, sentence_encoder_model)
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    model.summary()


def load_corpus(pos_filename, neg_filename):
    """加载正面和负面语料库
    Args:
        pos_filename: 正面文件名
        neg_filename: 负面文件名

    """
    with open(pos_filename, encoding='utf8') as r:
        pos_x = [line.strip() for line in r.readlines()]


    with open(neg_filename, encoding='utf8') as r:
        neg_x = [line.strip() for line in r.readlines()]

    pos_y = [1] * len(pos_x)
    neg_y = [0] * len(neg_x)
    return (pos_x+neg_x, pos_y+neg_y)


