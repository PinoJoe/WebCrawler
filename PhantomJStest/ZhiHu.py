# -*- coding: utf-8 -*-

import re
import requests

def get_xsrf(session):
    '''_xsrf是一个动态变化的参数，从网页中提取'''
    index_url = 'http://www.zhihu.com'
    #获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    #这里的_xsrf返回的是一个list
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]

agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {'User-Agent': agent}
session = requests.session()
_xsrf = get_xsrf(session)
post_url = 'http://www.zhihu.com/login/phone_num'
postdata = {
            '_xsrf': _xsrf,
            'password': 'qiaonan0116'
            'remember_me': 'true',
            'phone_num': '13608916056'
        }
login_page = session.post(post_url, data=postdata, headers=headers)
login_code = login_page.text
print(login_page.status_code)
print(login_code)
