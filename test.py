# str = 'hello world'
# print(str.__sizeof__())
#
# str1 = u'hello world'
# print(str1.__sizeof__())

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]

list_arr = zip(attributes, values)
# print(dict(list_arr))

# 多行
item = []
for value in values:
    temp = {}
    for j in range(len(value)):
        temp.update({attributes[j]:value[j]})
    item.append(temp)
print(item)

# 一行
print([dict(zip(attributes, x)) for x in values])


arr = {1:'1111',2:'2',3:'3',4:'2'}
arr.__delitem__(1)
print(arr)
