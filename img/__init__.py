#-*-coding:utf-8 -*-
import urllib
from lxml import etree
import requests
from time import perf_counter
def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100 :
        per = 100
    print('当前下载进度: %d' %per)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:58.0) Gecko/20100101 Firefox/58.0'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
h = etree.HTML(r.text)
img_urls = h.xpath('.//img/@src')
i = 0
for img_url in img_urls:
    urllib.request.urlretrieve(img_url, 'img'+str(i)+'.jpg', Schedule)
    i+=1