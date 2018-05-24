# -*- coding: utf-8 -*-

import requests
class HtmlDownloader:
    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windowns Nt 6.1; rv:59.0) Gecko/20100101 Firefox/59.9)'
        headers = {'User-Agent':user_agent}
        r = requests.get(url,headers=headers)
        if r.status_code==200:
            r.encodeing='utf-8'
            return r.text
        return None
