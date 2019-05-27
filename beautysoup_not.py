# beautifulsoup
# pip3 install bs4 安装命令

# pip3 install lxml

from bs4 import BeautifulSoup as bs

html_doc = ''
doc = bs(html_doc, 'lxml')
print(doc.prettify()) # 格式处理




