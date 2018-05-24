#-*-coding:utf-8 -*-

from lxml import etree
import requests
from urllib import error

def getjoke(self):
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:58.0) Gecko/20100101 Firefox/58.0'
    headers = {'User-Agent': user_agent}
    
    req = requests.get(self, headers=headers)
    response = etree.HTML(req.text)
    content = response.xpath('.//*[@class="content"]/span/text()')

    for div_content in content:
        print(div_content)
        with open('joke.txt', 'a', encoding='utf-8') as f:
            f.write(div_content)

i = 1
while i <= 13:
    url = 'http://www.qiushibaike.com/text/page/' + str(i)
    getjoke(url)
    i += 1