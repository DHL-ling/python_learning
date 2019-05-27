# Pandas库数据预处理和清洗
# pip3 install pandas 安装命令

import numpy as np
from numpy import nan
from pandas import Series, DataFrame  # 最重要的库
import pandas as pd


# series基本操作
data = Series([4, 5, 6, 7])
print(data)
# 输出结果，第一位为索引位置
# 0    4
# 1    5
# 2    6
# 3    7
# dtype: int64

print(data.index)  # RangeIndex(start=0, stop=4, step=1)
print(data.values)  # [4 5 6 7]

# 指定索引
obj = Series([4, 7, -6, 3], index=['a', 'b', 'c', 'd'])
obj['a'] = 6
print(obj)
print('f' in obj)  # 判断f是否在index索引中

# 字典转换成series
sdata = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
obj2 = Series(sdata)
print(obj2)

obj2.index = ['ab', 'cd', 'ef', 'hh']
print(obj2)

# DataFrame基本操作
frame = {
    'city': ['hangzhou', 'shanghai', 'shenzheng', 'gaungzhou', 'huzhou'],
    'year': [2020, 2019, 2016, 2017, 2003],
    'date': [2, 3, 1, 7, 5]
}
frame_data = DataFrame(frame)
print(frame_data)  # 输出类似与电子表格

# 根据columns内的字段将frame内的数据先后输出
frame2 = DataFrame(frame, columns=['year', 'date', 'city'])
print(frame2)

# 提取某个具体一列
print(frame2['city'])
print(frame2.year)

# 生成新的一列
frame2['new'] = [1, 2, 3, 4, 5]
print(frame2)

frame2['new2'] = frame2.city == 'hangzhou'
print(frame2)


# 行列索引对换
pop = {
    'hangzhou': {2008: 1.5, 2009: 1.4},
    'huzhou': {2009: 3.3, 2008: 3.6}
}
frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)


# 填充数值
obj3 = Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])
obj4 = obj3.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=10)  # 重新指定索引
print(obj4)


obj5 = Series(['blue', 'red', 'yellow'], index=[0, 2, 4])
print(obj5.reindex(range(6), method='ffill'))  # method指定填充内容，'ffill'用上面的数据填充


# 删除缺失数据
data_nan = Series([1, nan, 2])
print(data_nan.dropna())

data_frame = DataFrame([[1, 2, 4], [1, nan, 3], [nan, nan, nan]])
print(data_frame.dropna())  # 删除所有出现nan的地方
print(data_frame.dropna(how='all'))  # 只删除有全部nan的地方
data_frame[4] = nan
print(data_frame)
print(data_frame.dropna(axis=1, how='all'))  # 删除整列都是nan

# 填充为na的地方
print(data_frame.fillna(99))
print(data_frame.fillna(88, inplace=True))


# 层次化索引
data1 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]])
print(data1)
print('--------------')
print(data1['b'])
print('--------------')
print(data1['a':'c'])
print('--------------')
print(data1.unstack()) # 一维转换成二维
print(data1.unstack().stack()) # 二维转换成一维
