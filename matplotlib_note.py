# 绘图工具
# pip3 install matplotlib 安装命令

import matplotlib.pyplot as plt

plt.plot([1,3,5], [4,8,10])
# 显示所画的图
plt.show()

import numpy as np

# x轴的定义域为 -3.14 ~3.14,中间隔了100个元素
x = np.linspace(-np.pi, np.pi, 1000)
p = plt.plot(x, np.sin(x))
plt.show()

# 绘制多个图
y = np.linspace(-np.pi*2, np.pi*2, 100)
plt.figure(1, dpi=50) # 创建图表1
for i in range(1,5): # 画四条线
    plt.plot(x, np.sin(x/i))
plt.show()

# 直方图
plt.figure(1, dpi=50) #创建图表，dpi代表图片精细度，dpi越大文件越大
data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data) # 只要传入数据，直方图就会统计数据出现的次数
plt.show()

# 散点图
z = np.arange(1,10)
fig = plt.figure()
plt.scatter(z,z,c='r', marker='o') # c='r'表示散点颜色为红色，marker表示指定形状为圆形
plt.show()

# 导入csv绘制图片
import pandas as pd
iris = pd.read_csv('./iris_training.csv')
print(iris.head())
# 绘制散点图
iris.plot(kind = 'scatter', x='120', y='4')
plt.show()