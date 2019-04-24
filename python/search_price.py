# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年04月24日 星期三 17时00分08秒


def d(p):
    return 1000 - 5*p


def s(p1, p2):
    p1, p2 = max(p1, p2), min(p1, p2)
    return p1*d(p1) + p2*(d(p2)-d(p1))


max_s, a, b = 0, 0, 0
for p2 in range(0, 100):
    ss = [s(p1, p2) for p1 in range(100, 200)]
    tmp = max(ss)
    if tmp > max_s:
        max_s = tmp
        index = ss.index(tmp)
        a, b = p2, index+100

print('max: ', max_s)
print('a: %d, b: %d' % (a, b))
