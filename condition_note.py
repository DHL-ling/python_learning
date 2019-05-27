
# if条件判断
zodiac = 'abcdefghijklmnopq'
year = int(input('please input birthday:'))
if zodiac[year % 12] == 'a':
    print('you choose 1....')
elif zodiac[year % 12] == 'b':
    print('you choose 2....')
else:
    print('you choose 3....')

# 循环语句
# for语句
for cz in zodiac:
    print(cz)

# 遍历输出1-12的数字
for i in range(13):
    print(i)

# 遍历输出1至11的数字
for i in range(1, 12):
    print(i)

# %s为替换变量
for j in range(2000, 2009):
    print('%s year is %s' %(j, zodiac[j%12]))

# while语句
# 输出结果：1 3 4 5
num = 0
while True:
    num = num + 1
    if num > 5:
        break
    elif num == 2:
        continue
    else:
        print(num)
