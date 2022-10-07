# 研究性学习项目（Research project)
 - by students from Tsinghua University High School
 - This project verifies Kepler's law by Observing Jupiter and calculating its data.
 - Lazy to write English README


<!-- TOC -->

- [研究性学习项目](#研究性学习项目)
  - [操作方法](#操作方法)
  - [开普勒三定律](#开普勒三定律)
    - [开普勒第一定律](#开普勒第一定律)
    - [开普勒第二定律](#开普勒第二定律)        
    - [开普勒第三定律](#开普勒第三定律)    
  - [实验原理](#实验原理)
  - [进度](#进度)
  - [联系方式](#联系方式)

<!-- /TOC -->

**小组成员(member)：**

- 张诗瑶、张天一、韩天远、严嘉哲、李胤辰

## 操作方法(Solution)

运行main.py

输入木星卫星位置信息

自动生成卫星位置变化图像

从而验证开普勒第三定律

## 开普勒三定律

### 开普勒第一定律

- 所有行星绕太阳的轨道都是椭圆，太阳在椭圆的一个焦点上。

### 开普勒第二定律

- 行星和太阳的连线在相等的时间间隔内扫过的面积相等。

### 开普勒第三定律

- a：半轴长 | T：周期 | k为常数

- $$
  \frac{a^3}{T^2}=k
  $$

## 实验原理

- 半长轴近似成半径
- 利用python拟合
  - scipy库里的optimize下的curve_fit函数进行拟合
- 利用拟合出的矢量图找到多组数据验证定律
- 大致就这样
- 详见(程序原理)[https://github.com/larryyan/JupiterAnalysis/ProgramDetail.md]
- 使用时只需打开curve fit实现的那个，leastsq实现并没有成功。（main是干啥的，不用管

## 进度

- 第一次观测观测（6.7）
- 论文初稿（6.7）
- Python拟合程序v1.0（6.22）
- 也不知道咋的就在暑假做完了。。。。。。

## 联系方式

* 邮件:[@严嘉哲](mailto:larry_yan2010@fox.com) |
    [@张诗瑶](mailto:) |
    [@张天一](mailto:) 
