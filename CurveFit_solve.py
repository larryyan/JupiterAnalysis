# -*- coding=utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import random
import xlrd

import datetime
import time

# y = A * sin(omega*x + phi)
X = np.array([0])
Y = np.array([0])
"""
A = 0.1
omega = 0.1
"""

TimeRow = []
Star = [[], [], [], []]


def f(X, omega, A, phi):
    return A * np.sin(omega * X + phi)


def draw():
    fig = plt.figure(figsize=(15, 10))

    x = np.linspace(X[0], X[len(X)-1], 100)

    param_bounds = ([20, 0.75, 0], [500, 1.5, 2*np.pi])  # 设定下界和上界
    pos = np.array([100, 1, 0])                     # init possible answer
    fita, fitb = optimize.curve_fit(f, X, Y, p0= pos, \
        bounds= param_bounds, maxfev= 100000000)

    omega, A, phi = fita

    print('A=', A, ' omega=', omega, ' phi=', phi, '\n', end= '')

    plt.plot(X, Y, 'rx', label=u'数据点')

    y = f(x, omega, A, phi)

    plt.plot(x, y, 'k--', label=u'拟合曲线')
    
    plt.xlim(int(X[0]), int(X[len(X)-1]+1))
    plt.ylim(int(Y[0]), int(Y[len(Y)-1]+1))

    plt.legend()

    ax = fig.add_subplot(111)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
    ax.set_xtricks(datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in TimeRow)


    plt.rcParams['font.sans-serif'] = ['SimHei']              # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False                # 正常显示负号

    plt.xlabel(u'时间')
    plt.ylabel(u'水平方向木星距离(百万千米)')


    plt.xticks(fontsize=20, rotation=70)
    plt.yticks(fontsize=20)
    # 刻度字体大小

    plt.savefig(fname= 'jupiter.svg', format='svg')
    plt.show()

    return None


def addTimeRow(numtuple=()):
    global TimeRow
    TimeRow.append(datetime.datetime(*numtuple))


def init():
    global X, Y
    global Star, TimeRow

    data = xlrd.open_workbook('excel/test.xlsx')
    table = data.sheets()[0]                                  #通过索引顺序获取
    ExcelTimeRow = table.row_values(0, start_colx= 1)
    for time in ExcelTimeRow:
        NumTuple = xlrd.xldate_as_tuple(time, data.datemode)
        addTimeRow(numtuple=NumTuple)

    print(TimeRow)

    for i in range(4):
        Star[i] = table.row_values(i + 1, start_colx= 1)
    
    return None


"""
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
"""


def main():
    global X, Y

    init()

    X = np.array(TimeRow)

    print(X)
    for i in range(4):
        Y = np.array(Star[i])
        draw()

        break
    
    return None
    


#    auto_init()
#    draw()


if __name__ == '__main__':
    main()
