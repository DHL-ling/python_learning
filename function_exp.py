
# f = open('example.txt')
# data = f.read()
# print(data.split('|'))

# def func(filename):
#     print(open(filename).read())
#
# func('name.txt')
import re
# def find_item(hero):
#     with open('example.txt') as f:
#         data = f.read().replace('\n', '')
#         name_num = re.findall(hero, data)
#     return len(name_num)
#
# name_dict = {}
# with open('name.txt') as f:
#     for line in f:
#         names = line.split('|')
#         for n in names:
#             num = find_item(n)
#             name_dict[n] = num

# 函数参数传递
# *表示可选参数
def howlong(first, *other):
    return 1 + len(first)

print(howlong('qqqq'))


# 函数作用域
var1 =  123
def func():
    #var1 = 222 # 只影响函数内
    global var1 # 全局作用，会更改外面变量
    var1 = 333
    print(var1)

func()
print(var1)

# 迭代器：iter
list1 = [1,2,3]
it = iter(list1)
print(next(it))
print(next(it))

# 生成器: yield
def frang(start, stop, step):
    x = start
    while x < stop:
        yield x # 运行到这个位置时会暂停，并记录到当前的位置
        x += step

for x in frang(10, 20, 0.5):
    print(x)

# lambda表达式
# lambda x: x <= (month, day)
# # 上面语句相当于下面的函数
# def funcLamda(x):
#     return  x <= (month, day)


# 内建函数
# filter
a = [1,2,3,4,5,6,7]
print(list(filter(lambda x:x>2, a))) # 返回列表内大于2的数

# map
a = [11,22]
b = [10, 20]
print(list(map(lambda x:x+1, a))) # 对a列表内的数都进行+1操作
print(list(map(lambda x, y:x+y,a,b))) # a列表与b列表对应位置的数累加，返回

# 使用reduce必须先导入reduce包
from functools import reduce
print(reduce(lambda x,y: x+y, [2,3,4],1)) # (((1+2)+3)+4)

# list对应位置组成新的列表:类似与矩阵转换
c = [1,2,3]
d = [4,5,6]
for i in zip(c, d):
    print(i)

# 将字典的key和value对调
dicta = {'a':'aa', 'b':'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dict(dictb))

# 内建函数如果有 _iter_为可迭代函数，能用for in取迭代值










