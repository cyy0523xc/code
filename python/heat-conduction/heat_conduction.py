#!/usr/bin/env python
# coding=utf-8

import math

# 常量定义说明:
# g1: 玻璃盖板1
# g2: 玻璃盖板2
# a:  环境
# b:  保温棉
# c:  电池
# w:  水

# 质量相关常量
m_g1 = 2.11        # 盖板1质量
m_g2 = 2.11        # 盖板2质量
m_b = 0.0214       # 保温棉的质量
m_c = 0.117        # 光伏电池的质量
C_w = 4174         # 水的比热容

# 比热容常量
C_g1 = 900         # 盖板1比热容
C_g2 = 900         # 盖板2比热容
C_c = 700          # 光伏电池的比热容
C_b = 841          # 保温棉的比热容

# 吸收率
a_g1 = 0.06        # 盖板1吸收率
a_g2 = 0.06        # 盖板2吸收率
a_w = 0.2          # 水的吸收率

# 传热系数
h_w_g1 = 148.2     # 盖板1与水之间的对流传热系数
h_w_g2 = 148.2     # 盖板2与水之间的对流传热系数
h_c_g2 = 899.3     # 盖板2与电池之间的传热系数
h_bc = 8.6         # 保温棉与电池之间的传热系数

# 其他常量
A = 0.236          # 盖板面积
G = 0              # 表面太阳光辐照度
m_w = 0.0467       # 系统水的质量流量
M_w = 8            # 水箱内水的总质量
R_g1 = 0.04        # 玻璃盖板1的反射率
R_ab = 101         # 水槽与环境的热阻


n = 100                # 循环次数
zeros = [.0] * (n+1)   # 生成n+1个全是0的列表, 因为计算温度时,会计算i+1, 所以需要生成n+1

# 初始化列表变量
V = zeros              # 风速
h_a_g1 = zeros         # 盖板1与环境之间的对流传热系数
T_in = zeros           # 进水口水的温度
T_g1 = zeros           # 盖板1温度的初始值
T_g2 = zeros           # 盖板2温度的初始值
T_w = zeros            # 水槽中的水温
T_a = zeros            # 环境温度 
T_b = zeros            # 保温棉温度
T_c = zeros            # 电池温度
E_c = zeros            # 电池功率
q_r_gl = zeros         # 盖板与环境之间的辐射换热量
mCT_in_out = zeros     # 水的能量平衡方程的左边部分
h_ab = zeros           # 保温棉与环境之间的对流传热系数


# 盖板与环境之间的辐射换热量
def cal_q_r_g1(T_a, T_g1):
    '''
    T_a : 环境温度
    T_g1: 盖板温度
    '''
    T_a_4 = T_a ** 4
    T_g1_4 = T_g1 ** 4
    q_r_gl = 0.236 * 0.9 * 5.67 * (10 ** -8) * (0.33 * (T_a_4 - T_g1_4) + 0.9 * ((0.0552 * (T_a ** 1.5)) ** 4 - T_g1_4) + 0.067 * (T_a_4 - T_g1_4))
    return q_r_gl

# 盖板与环境之间的对流传热系数
def cal_h_a_g1(T_g1, T_a, V):
    '''
    T_a : 环境温度
    T_g1: 盖板温度
    V   : 风速
    '''
    h_a_g1 = math.sqrt(2.15 * (T_g1 - T_a) ** (2/3) + (2.38 * V ** 0.89) ** 2)
    return h_a_g1

# 光伏电池的输出功率
def cal_E_c(G, T_c):
    '''
    G   : 光照强度
    T_c : 光伏电池温度
    '''
    E_c = 0.0241 * G * (1 - 0.0045 * (T_c - 298.15))
    return E_c

# 保温棉与环境之间的对流传热系数
def cal_h_ab(T_b, T_a, V):
    '''
    T_b  : 保温棉温度
    T_a  : 环境温度
    V    : 风速
    '''
    h_ab = math.sqrt(0.681 * (T_b - T_a) ** 2 + (2.38 * V ** 0.89) ** 2)
    return h_ab

# 循环n次
for i in range(0, n-1):
    # 盖板与环境之间的对流传热系数
    h_a_g1[i] = cal_h_a_g1(T_g1[i-1], T_a[i], V[i])

    # 盖板与环境之间的辐射换热量
    q_r_gl[i] = cal_q_r_g1(T_a[i], T_g1[i])

    # 玻璃盖板1的能量平衡方程 
    T_g1[i+1] = T_g1[i] + (G * A * a_g1 + h_a_g1[i] * A * (T_a[i] - T_g1[i]) + h_w_g1 * A * (T_w[i] - T_g1[i]) + q_r_gl[i]) * 10 / (m_g1 * C_g1)

    # 水的能量平衡方程
    mCT_in_out[i] = (h_w_g1 * A * (T_g1[i] - T_w[i]) + h_w_g2 * A * (T_g2[i] - T_in[i]) + 0.94 * G * A * (1 - R_g1) * a_w) * 10

    # 玻璃盖板2的能量平衡方程
    T_g2[i+1] = T_g2[i] + (h_w_g2 * A * (T_in[i] - T_g2[i]) + h_c_g2 * A * (T_a[i] - T_g2[i]) + 0.43 * G * A) * 10 / (m_g2 * C_g2)

    # 光伏电池层能量平衡
    E_c[i] = cal_E_c(G, T_c[i])
    T_c[i+1] = T_c[i] + (h_c_g2 * A * (T_g2[i] - T_c[i]) + h_bc * A * (T_b[i] - T_c[i]) + 0.636 * G * A - E_c[i]) * 10 / (m_c * C_c)

    # 保温棉的能量平衡方程
    h_ab[i] = cal_h_ab(T_b[i], T_a[i], V[i])
    T_b[i+1] = T_b[i] + (h_bc * A * (T_c[i] - T_b[i]) + h_ab[i] * A * (T_a[i] - T_b[i])) * 10 / (m_b * C_b)

    # 水箱传热模型
    T_w[i+1] = T_w[i] + ((T_a[i] - T_w[i]) / R_ab + mCT_in_out[i]) * 10 / (M_w * C_w)


print '电池背板温度是: '
print T_c 

print '电池功率是: '
print E_c

print '水温是: '
print T_w

