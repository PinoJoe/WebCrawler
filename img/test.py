#-*-coding:utf-8 -*-
import urllib
from lxml import etree
import requests
import time
from contextlib import closing

def ProcessBar(blocknum, blocksize, totalsize):
    speed = (blocknum * blocksize) / (time.time() - start_time)
    speed_str = '下载速度： %s' % format_size(speed)
    recv_size = blocknum * blocksize
    pervent = recv_size / totalsize
    percent_str = '%.2f%%' % (pervent * 100)
    n = round(pervent * 5)
    s = ('=' * n).ljust(5, '-')
    print(percent_str.ljust(8, ' ') + '[' + s + ']' + speed_str, end='\r')

def format_size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print('传入的字节格式错误')
        return 'Error'
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return '%.3fG' % (G)
        else:
            return '%.3fM' % (M)
    else:
        return '%.3fK' % (kb)

user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:58.0) Gecko/20100101 Firefox/58.0'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
h = etree.HTML(r.text)
img_urls = h.xpath('.//img/@src')
i = 0
for img_url in img_urls:
    filename = 'img' + str(i) + '.jgp'
    start_time = time.time()
    urllib.request.urlretrieve(img_url, filename, ProcessBar)
    i += 1
    print('\n')
