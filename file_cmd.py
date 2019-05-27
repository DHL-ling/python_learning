# linux操作命令
# ls 查看文件
# ls -l 区分文件类型
# pwd 查看当前所在的位置
# cd ..当对路径
# mkdir 新建文件夹
# mkdir -p
# rm 删除文件夹
# rm -rf 删除文件及下面所有的内容

import os

print(os.path.abspath('.')) # 当前文件的路径
print(os.path.exists('tmp')) # 判断文件或者目录是否存在
print(os.path.isdir('tmp')) # 是否有这个路径
print(os.path.join('/tmp/s', 'aa')) # 连接路径

from pathlib import Path

p = Path('.')
Path.mkdir('/tmp/s', parents=True)
