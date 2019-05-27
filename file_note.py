# 打开文件：open()
# 输入：read()
# 输入一行： readline()
# 文件内移动 seek()
# 输出write()
# 关闭文件close()

# file1 = open('name.txt', 'w')
# file1.write('ddddd')
# file1.close()
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt', 'a')
# file3.write('bbbb')
# file3.close()

file4 = open('name.txt')
print(file4.readline())

# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)


# 指定文件已什么编码方式打开
f3 = open('name.txt', encoding='GB18030')

# 指针
file6 = open('name.txt')
print('当前文件指针的位置 %s' %file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
# 第一个参数代表偏移位置，第二个参数表示从文件开头偏移
file6.seek(5,0)
print('我们进行了seek操作')
print('当前文件指针的位置 %s' %file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
file6.close()