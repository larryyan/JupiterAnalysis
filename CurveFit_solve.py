# -*- coding=utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import random
import xlrd

import datetime
import time

# y = A * sin(omega*x + phi)
X = np.array([])
Y = np.array([])
"""
A = 0.1
omega = 0.1
"""

TimeRow = []
Star = [[], [], [], []]
tempx = []


def f(X, omega, A, phi):
    return A * np.sin(omega * X + phi)


def draw():
    fig = plt.figure(figsize=(15, 10))
    fig1, ax = plt.subplots()

    x = np.linspace(X[0], X[len(X)-1], 20)
    listxnumber = x.tolist()
    listxdatetime = [datetime.datetime.fromtimestamp(i * 1000) for i in listxnumber]
    timex = np.array([d.strftime('%Y-%m-%d %H:%M:%S') for d in listxdatetime])
    # print(timex, x)

    param_bounds = ([0, 0.9, 0], [1, 1.5, 2*np.pi])  # 设定下界和上界
    pos = np.array([0.8, 1, 0])                     # init possible answer
    fita, fitb = optimize.curve_fit(f, X, Y, p0= pos, bounds= param_bounds, maxfev= 100000000)

    omega, A, phi = fita

    print('A=', A, ' omega=', omega, ' phi=', phi, '\n', end= '')

    y = f(x, omega, A, phi)

    # plt.plot(TimeRow, Y, 'rx', label=u'数据点')
    ax.plot(Y, 'rx', label=u'数据点')

    # plt.plot(timex, y, 'k--', label=u'拟合曲线')
    ax.plot(y, 'k--', label=u'拟合曲线')

    # plt.xlim(int(min(X)), int(max(X)))
    # plt.ylim(int(min(Y)), int(max(Y)))

    plt.legend()

    plt.rcParams['font.sans-serif'] = ['SimHei']              # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False                # 正常显示负号

    xticks = list(range(0, len(TimeRow), 3))
    xlabels = [TimeRow[x] for x in xticks]
    xticks.append(len(TimeRow))
    xlabels.append(TimeRow[-1])

    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)

    plt.xlabel(u'时间')
    plt.ylabel(u'水平方向木星距离(百万千米)')

    plt.xticks(fontsize=10, rotation=270)
    plt.yticks(fontsize=20)
    # 刻度字体大小

    plt.show()
    plt.savefig(fname= 'jupiter.svg', format='svg')

    return None


def addTimeRow(numtuple=()):
    global TimeRow, tempx
    timerowdatetime = (datetime.datetime(*numtuple))
    TimeRow.append(timerowdatetime.strftime('%Y-%m-%d %H:%M:%S'))
    tempx.append(time.mktime(datetime.datetime(*numtuple).timetuple()))

    return None


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

    X = np.array(tempx) / 1000

    # (X)
    for i in range(4):
        Y = np.array(Star[i])
        draw()

        break
    
    return None
    


#    auto_init()
#    draw()


if __name__ == '__main__':
    main()
