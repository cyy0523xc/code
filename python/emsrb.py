# -*- coding: utf-8 -*-
#
# EMSRb算法
# Author: alex
# Created Time: 2019年04月19日 星期五 16时31分29秒
import math
import numpy as np
from scipy.stats import norm


def EMSRb(prices, mean, var, cap, alpha=0):
    """
    Args:
        prices: 价格等级
        mean: 需求均值
        var: 需求方差
        cap: 总座位数
        alpha: 向上购买因子。当得不到折扣座位时，被拒绝的需求会转为更高票价的概率，0<=alpha<1
    """
    tmp = [(p, m, v) for p, m, v in zip(prices, mean, var)]
    tmp = sorted(tmp, key=lambda x: x[0], reverse=True)
    prices = np.array([t[0] for t in tmp])
    mean = np.array([t[1] for t in tmp])
    var = np.array([t[2] for t in tmp])
    y, alpha_t = [], 1/(1-alpha)
    for j in range(1, len(prices)):
        sum_mean = sum(mean[:j])
        sigma = math.sqrt(sum(var[:j]))
        p = sum(mean[:j]*prices[:j]) / sum_mean
        tmp = norm.ppf(alpha_t*(1 - prices[j]/p))
        yi = sum_mean + sigma * tmp
        y.append(min(yi, cap))

    y.append(cap)
    return np.ceil(y)


if __name__ == '__main__':
    prices = (1050, 950, 699, 520)
    mean = (17.3, 45.1, 39.6, 34.0)
    var = np.array((5.8, 15.0, 13.2, 11.3))**2
    cap = 130
    print(EMSRb(prices, mean, var, cap))  # [ 10.  54.  97. 130.]
    print(EMSRb(prices, mean, var, cap, alpha=0.1))  # [ 10.  54.  97. 130.]
