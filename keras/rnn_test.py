# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2017年12月24日 星期日 16时09分10秒
# please note, all tutorial code are running under python3.5.
# If you use the version like python2.7, please modify the code accordingly

# 8 - RNN LSTM Regressor example

# to try tensorflow, un-comment following two lines
# import os
# os.environ['KERAS_BACKEND']='tensorflow'
import time
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, TimeDistributed, Dense
from keras.optimizers import Adam

BATCH_START = 0
TIME_STEPS = 20
BATCH_SIZE = 50
INPUT_SIZE = 1
OUTPUT_SIZE = 1
CELL_SIZE = 20
LR = 0.006

np.random.seed(1337)  # for reproducibility


def get_batch():
    global BATCH_START, TIME_STEPS
    # xs shape (50batch, 20steps)
    xs = np.arange(BATCH_START, BATCH_START+TIME_STEPS*BATCH_SIZE)\
        .reshape((BATCH_SIZE, TIME_STEPS)) / (10*np.pi)
    seq = np.sin(xs)
    res = np.cos(xs)
    BATCH_START += TIME_STEPS
    # plt.plot(xs[0, :], res[0, :], 'r', xs[0, :], seq[0, :], 'b--')
    # plt.show()
    return [seq[:, :, np.newaxis], res[:, :, np.newaxis], xs]


def create_model():
    # build a LSTM RNN
    model = Sequential()
    model.add(LSTM(
        batch_input_shape=(BATCH_SIZE, TIME_STEPS, INPUT_SIZE),       # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,
        output_dim=CELL_SIZE,
        return_sequences=True,      # True: output at all steps. False: output as last step.
        stateful=True,              # True: the final state of batch1 is feed into the initial state of batch2
    ))

    # add output layer
    model.add(TimeDistributed(Dense(OUTPUT_SIZE)))
    adam = Adam(LR)
    model.compile(optimizer=adam,
                loss='mse',
                )

    return model


def rnn():
    model = create_model()
    print('Training ------------')
    for step in range(501):
        # data shape = (batch_num, steps, inputs/outputs)
        x_batch, y_batch, xs = get_batch()
        cost = model.train_on_batch(x_batch, y_batch)
        pred = model.predict(x_batch, BATCH_SIZE)
        plt.plot(xs[0, :], y_batch[0].flatten(), 'r', xs[0, :], pred.flatten()[:TIME_STEPS], 'b--')
        plt.ylim((-1.2, 1.2))
        plt.draw()
        plt.pause(0.1)
        if step % 10 == 0:
            #print(x_batch)
            #print(y_batch)
            #print(xs)
            print('train cost: ', cost)


if __name__ == '__main__':
    rnn()
    time.sleep(100)
