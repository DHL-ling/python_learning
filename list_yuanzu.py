#列表
l = [3, 2, 3, 7, 8, 1]
print(l.__sizeof__())
l.count(3)  #2  表示统计列表 / 元组中 item 出现的次数
l.index(7) #3 index(item) 表示返回列表 / 元组中 item 第一次出现的索引
# list.reverse() 和 list.sort() 分别表示原地倒转列表和排序(注意，元组没有内置的这两个函数)。
l.reverse() #l [1, 8, 7, 3, 2, 3]
l.sort() #l [1, 2, 3, 3, 7, 8]

# 元组
tup = (3, 2, 3, 7, 8, 1)
tup.count(3) #2
tup.index(7) #3
# reversed() 和 sorted() 同样表示对列表/ 元组进行倒转和排序但是会返回一个倒转后或者排好序的新的列表 / 元组。
list(reversed(tup)) #[1, 8, 7, 3, 2, 3]
sorted(tup) #[1, 2, 3, 3, 7, 8]

print(7 in tup)

l = ['a333', 's33', 's33']
print(l.__sizeof__())

# 字典
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')

# 集合
s1 = {1, 2, 3}
# d1[0] || s1[0] 报错，不支持索引
print('ss' in s1)
s2 = set([1, 2, 3])

# 字典和集合支持增删改等操作
d = {'name': 'jason', 'age': 20}
d['gender'] = 'male' # 增加元素对'gender': 'male'
d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
#d{'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
d['dob'] = '1998-01-01' # 更新键'dob'对应的值
d.pop('dob') # 删除键为'dob'的元素对
#'1998-01-01'
#d{'name': 'jason', 'age': 20, 'gender': 'male'}

s = {1, 2, 3}
s.add(4) # 增加元素 4 到集合
#s{1, 2, 3, 4}
s.remove(4) # 从集合中删除元素 4
#s{1, 2, 3}


d = {'name': 'jason', 'education': ['Tsinghua University', 'Stanford University']}
print(d)



