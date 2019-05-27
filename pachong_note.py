# 网页数据采集
from urllib import request
from urllib import parse

# 获取网页内容
url = 'http://www.baidu.com'
re = request.urlopen(url, timeout=5) # timeout 设置超时时间
#print(re.read().decode('utf-8')) # 编码转换

# post and get 请求
try:
    data = bytes(parse.urlencode({'aa', 'bb'}), encoding='utf8')
    test = request.urlopen('http://www.baidu.com/post', data=data)
    print(test.read().decode('utf-8'))
except Exception as e:
    print(e)

# http头部信息获取


