# -*- coding: utf-8 -*-
# @author cyy0523xc@gmail.com

from scipy.stats import norm
from math import *


def delta(q, K, T, S0, r, sigma):
    """
    Delta值：衡量标的证券价格变动对期权价格的影响程度

    params:
        q:  股息率
        K:  期权行权价格
        T:  剩余期限（年化）
        S0: 标的收盘价
        r:  无风险收益率
        sigma: 波动率（年化）

    return:
        delta_call 看涨期权
        delta_put  看跌期权
    """
    n_d1 = N(d1(S0, K, r, q, sigma, T))
    e_qt = e ** (-q * T)
    delta_call = n_d1 * e_qt
    delta_put = (n_d1 - 1) * e_qt
    return (delta_call, delta_put)


def N(x):
    """标准正态分布的累积分布函数"""
    return norm.cdf(x)


def d1(S0, K, r, q, sigma, T):
    return (log(S0 / K) + (r - q + (sigma ** 2) / 2) * T) / (sigma * sqrt(T))


def d2():
    return


if __name__ == "__main__":
    params = [
        {
            "q": 0,
            "K": 2.0,
            "T": 12.0 / 365.0,
            "S0": 2.085,
            "r": 0.045,
            "sigma": 0.1213
        },
        {
            "q": 0,
            "K": 2.5,
            "T": 0.076712,
            "S0": 2.638,
            "r": 1,
            "sigma": 0.2764
        },
        {
            "q": 0,
            "K": 2.5,
            "T": 0.076712,
            "S0": 2.638,
            "r": 1,
            "sigma": 0.2764
        },
        {
            "q": 0.03,
            "K": 2.5,
            "T": 0.249315,
            "S0": 2.638,
            "r": 8,
            "sigma": 0.2572
        },
        {
            "q": 0.03,
            "K": 2.5,
            "T": 0.249315,
            "S0": 2.638,
            "r": 8,
            "sigma": 0.2572
        },
        {
            "q": 0,
            "K": 2.8,
            "T": 0.49863,
            "S0": 2.638,
            "r": 8,
            "sigma": 0.2572
        }
    ]

    res = [delta(p['q'], p['K'], p['T'], p['S0'], p['r'], p['sigma'])
           for p in params]
    print res
