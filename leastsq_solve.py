# -*- coding:utf-8 -*-

# by larryyan
# from 2020/5/24 19:30
# to

# 导入函数库
import numpy as np
import matplotlib.pyplot as plt

# 导入最小二乘拟合库
from scipy.optimize import leastsq
# 导入数据加噪声的库
from scipy.stats import norm


# 固定参数
a = 0.1
omega = 0.1

# 输入的数据
input_x = []
input_y = []


# 定义原函数
def function(x, phi):
    result = a * np.sin(omega * x + phi)
    return result


# 定义误差函数，将要优化的参数放在前面
def f_err(y, x, phi):
    return y - function(x, phi[0])


# 绘图
def draw():

    plt.rcParams["font.family"] = "SimHei"
    plt.rcParams["axes.unicode_minus"] = False

    # 把x、y数字转化为numpy数组
    x = np.array(input_x)
    y = np.array(input_y)

    c = [0.001]

    # 将这个函数作为参数传入 leastsq 函数，第二个参数为初始值
    r = leastsq(f_err, *c, args=(y, x), full_output=True)
    solution = r[0]
    cov_x = r[1]
    infodict = r[2]
    mesg = r[3]
    ier = r[4]
    if ier >= 1 and ier <= 4:
        print('succeed')
    print(mesg)
    print('拟合phi:', solution)
    print(infodict)

    # 绘制图像
    p = plt.plot(x, y, 'rx', label='原始数据点')
    p = plt.plot(x, function(x, *c), 'k--', label='拟合曲线')

    # 显示图像
    plt.legend()
    plt.show()

    return None


# 输入x，y
def get_xy():
    global input_x, input_y
    n = int(input('请输入数据组数：'))
    # 输入x列表
    for i in range(n):
        xi = eval(input('x%d: ' % i))
        input_x.append(xi)
    # 输入y列表
    for i in range(n):
        yi = eval(input('y%d: ' % i))
        input_y.append(yi)

    return None


# 生成x, y
def create_xy():
    global input_x, input_y
    for i in range(30):
        input_x.append(i * 10)
    # 输入phi
    phi = eval(input('phi: '))
    for i in input_x:
        input_y.append(function(i, phi))
    # 加入噪声
    x = np.array(input_x)
    y = np.array(input_y)
    y_noisy = y + 0.09 * norm.rvs(size=len(x))
    input_y = y_noisy.tolist()


def getdata():
    global a, omega
    # 输入 振幅（轨道半径 or 卫星与木星距离）
    a = eval(input('a: '))
    # 输入 周期（绕木星运行一圈的时间）
    t = eval(input('t: '))
    # omega = 2pi/T
    omega = 2 * np.pi / t
    '''
    # 输入 x, y
    get_xy()
    '''
    # 生成 x, y
    create_xy()


# 主函数
def main():
    getdata()
    draw()
    return None


if __name__ == '__main__':
    main()
