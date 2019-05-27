# 变量的定义
x = 200
print(x / 8)

# 序列
# 序列的分片操作符: [:]
zodiac = '123456'
print(zodiac[0:4])
print(zodiac[-1])
print(zodiac[-3:-1])
print(zodiac[-3:])

# 序列成员操作关系
print('1' in zodiac)
print('1' not in zodiac)

# 序列的连接操作: +
print(zodiac + 'ssss')

# 字符串和数字连接，系统报错
# print(zodiac + x)

# 字符串重复操作符：*
print(zodiac * 3)

print('no data available for person with id: %d, name: %s' % (11, 2222))
print('no data available for person with id: {}, name: {}'.format(111, '222'))


# 元组与列表的区别：元组一般不可变更；列表可变更

# 列表
a_list = ['abc', 'xyz']
a_list.append('ZZZ')
# a_list.remove('xyz')
print(a_list[0: 2])

# 元组
# u 表示 unioncode
zodiac_name = (u'双子座', u'处女座', u'双鱼座', u'摩羯座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21))

# 两个元组的比较，相当于啊 120>219 return false
print((1, 20) > (2, 19))

# 取出元组days中,比(month, day)小的数
(month, day) = (1, 23)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(list(zodiac_day))  # 执行结果为（1，20）

zodiac_len = len(list(zodiac_day))
print(zodiac_len)

# 字典: 映射类型
dict = {}
print(type(dict))

dict2 = {'x': 1, 'y': 2}
dict2['z'] = 3
dict2['y'] = 4
print(dict2)

dict3 = {
    'a': {
        'key': 11,
        'value': 'aaaaa'
    },
    'b': {
        'key': 22,
        'value': 'bbbbb'
    }
}
print(dict3)
