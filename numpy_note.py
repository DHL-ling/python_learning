# 安装numpy命令：pip3 install numpy
import numpy as np

# 数组与数据类型
arr1 = np.array([1,2,3,4])
print(arr1.dtype) # int64

arr2 = np.array([1.2, 2.2])
print(arr2.dtype) # float64

arr3 = np.array([4,5,6,7])
print(arr1 + arr3) # [ 5  7  9 11]

# 数组和标量计算
print(arr2 * 10) # [12.

# 矩阵转换
data = [[1,2,3], [4,5,6]]
arr3 = np.array(data)
print(arr3)

# 自定义一个矩阵
np.zeros(10) # 一维矩阵
np.zeros((3,5)) # 3*5的维矩阵，里面都为0
np.ones((4,6)) # 4*6的矩阵，里面都为1
print(np.zeros((4,6)))
print(np.empty((2,3,2))) # 2*3*2三维矩阵,随机填充数据

# 数组的索引和切片
arr4 = np.arange(10) # 输出0-10的数字
print(arr4[3:5]) # 输出第三位至第五位的值

#给特定位置赋值
# arr4[5:8] = 44
# print(arr4)

#重新赋值，不改变原有赋值
arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr4)

