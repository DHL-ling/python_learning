# seaborn
# pip3 install seaborn 安装命令

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings

iris = pd.read_csv('./iris_training.csv')
# 设置样式
sns.set(style='red', color_codes=True)
# 设置绘制格式散点图
sns.jointplot(x='120', y='4',data=iris, size=5)
# distplot绘制曲线
sns.distplot(iris['120'])
plt.show()