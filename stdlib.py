# 日常应用比较广泛的模块是：
# 1. 文字处理的 re
# 2. 日期类型的time、datetime
# 3. 数字和数学类型的math、random
# 4. 文件和目录访问的pathlib、os.path
# 5. 数据压缩和归档的tarfile
# 6. 通用操作系统的os、logging、argparse
# 7. 多线程的 threading、queue
# 8. Internet数据处理的 base64 、json、urllib
# 9. 结构化标记处理工具的 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的venv
# 13. 运行服务的__main__


import re
# . ^ $ * + ? {m} {m,n} [] |  \d \D \s ()
# . 匹配任意单个字符
# ^ 匹配已某个字符为开头
# $ 匹配已某个字符为结尾
# * 匹配前面的字符从0次到多次
p = re.compile('cat*t')
print(p.match('cat'))
# + 匹配前面的字符1次到多次
# ? 匹配字符出现0次或者1次
# {m} 前面的字符指定出现m次
# {m,n} 前面的字符指定出现m到n次
# [] 匹配里面的任意一个字符
# \d 匹配的内容为一串数字
# \D 匹配内容不包含数字
# \s 匹配是否为一个字符串
# () 进行分组

# ^$ 表示是否为空行
# .*? 不使用贪婪模式

str = re.compile('(\d+)-(\d+)-(\d+)')
print(str.match('2018-10-11').group(1))
print(str.match('2018-10-11').groups())
print(str.search('a2018-10-11'))

# re.sub('被替换的值', '替换的值', '替换的字符串')
print(re.sub(8, 9, str))