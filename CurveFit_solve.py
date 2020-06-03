# -*- coding=utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import random

# y = A * sin(omega*x + phi)
X = np.array([0])
Y = np.array([0])
A = 0.1
omega = 0.1


def f(X, phi):
    return A * np.sin(omega * X + phi)


def draw():
    plt.figure(figsize=(15, 10))
    x = np.linspace(0, 1000, 1000)

    param_bounds = ([0], [2*np.pi])  # 设定下界和上界
    fita, fitb = optimize.curve_fit(f, X, Y, bounds= param_bounds)
    phi = fita[0]

    print('A=', A, ' omega=', omega, ' phi=', phi, '\n', end= '')

    plt.scatter(X, Y, s=100, alpha=1.0, marker='x', label=u'数据点')

    y = f(x, phi)

    ax = plt.gca()  # gca获取轴这个对象

    ax.set_xlabel(..., fontsize=20)
    ax.set_ylabel(..., fontsize=20)
    # 设置坐标轴标签字体大小

    plt.plot(x, y, color='r', linewidth=3, linestyle="-", markersize=5, label=u'拟合曲线')

    plt.legend(loc=0, numpoints=1)
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize='xx-large')

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

    plt.xlabel(u'时间(分钟)')
    plt.ylabel(u'y(10^8米)')

    plt.xlim(0, x.max() * 1.1)
    plt.ylim(y.min() * 0.9, y.max() * 1.1)

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    # 刻度字体大小

    plt.savefig(fname= 'jupiter.svg', format='svg')
    plt.show()


def init():
    global X, Y
    n = int(input('组数：'))
    tx = []
    ty = []
    for i in range(n):
        x = int(input('x: '))
        y = int(input('y: '))
        tx.append(x)
        ty.append(y)
    X = np.array(tx)
    Y = np.array(ty)


def auto_init():
    global X, Y, A, omega
    A = eval(input('轨道半径（10^8米）：'))
    T = eval(input('轨道周期（分钟）：'))
    start_time = eval(input('开始观测时间：'))
    end_time = eval(input('结束观测时间：'))
    time_interval = eval(input('观测时间间隔：'))
    omega = 2 * np.pi / T
    phi = random.uniform(0, 2 * np.pi)
    X = np.arange(start_time, end_time, time_interval)
    Y = A * (np.sin(omega * X + phi) + np.random.rand() * 1 - 0.2)
    print(X, '\n', Y)
    print('A=', A, ' omega=', omega, ' phi=', phi, '\n', end= '')


def main():
    # init()
    auto_init()
    draw()


if __name__ == '__main__':
    main()
