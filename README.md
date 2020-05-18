[TOC]

#  程序部分

## 引进基础包

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import random
```



## 初始化数据

```python
X = np.array([0])
Y = np.array([0])
A = 0.1
omega = 0.1

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
```

## 正弦函数拟合

### 定义画布

```python
plt.figure(figsize=(15, 10))
x = np.linspace(0, 1000, 1000)
```

### 定义函数

![image-20200518231132495](img\image-20200518231132495.png)

```python
def f(X, phi):
    return A * np.sin(omega * X + phi)
```

### 绘制散点

```python
plt.scatter(X, Y, s=100, alpha=1.0, marker='x', label=u'数据点')
```

### 拟合正弦函数

#### 拟合得出函数参数

这里我们使用的是python中scipy模块的子模块optimize中提供了一个专门用于曲线拟合的函数**curve_fit()**。

这是基于**广义逆的最小二乘曲线拟合**，采用**满秩分解**。

```python
param_bounds = ([0], [2*np.pi])  # 设定下界和上界
fita, fitb = optimize.curve_fit(f, X, Y, bounds= param_bounds)
phi = fita[0]
```

fita为函数各参数

fitb为协方差矩阵

#### 绘制拟合的函数

```python
ax = plt.gca()  # gca获取轴这个对象

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
# 设置坐标轴标签字体大小

plt.plot(x, y, color='r', linewidth=3, linestyle="-", markersize=5, label=u'拟合曲线')
```
## 图像显示

```python
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
```

# 整体程序

```python
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


def solve():
    init()
    draw()


solve()
```

