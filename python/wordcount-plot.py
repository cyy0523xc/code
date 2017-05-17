# -*- coding: utf-8 -*-

# 将词频进行可视化
# Author: Alex
# Created Time: 2017年03月20日 星期一 23时43分12秒

import matplotlib.pyplot as plt


# 这是统计好的数据
data = [('Learn', 1), ('is', 1), ('spark', 2), ('This', 1), ('time', 1)]

plt.xlabel(u"词频")
plt.ylabel(u"单词")
plt.title(u"词频统计")

x = [i[0] for i in data]
y = [i[1] for i in data]
index = [i for i in range(len(data))]

plt.xticks(index, x)
plt.bar(left=index, height=y, align="center")
plt.show()
