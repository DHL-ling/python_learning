# pip3 install requests

import requests

# get
url = 'http://baidu.com/get'
data = {}
re = requests.get(url,data)
print(re.text)

# post
re2 = requests.post(url,data)
re2.json() # 返回类型为json格式

# 爬取网页数据

pic = requests.get('').text
print(pic)