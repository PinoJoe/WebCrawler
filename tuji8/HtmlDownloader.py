# -*- coding: utf-8 -*-
import requests
import urllib
import time

class HtmlDownloader:

    def download_page(self, page_url):
        if page_url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'
        header = {'User_Agent':user_agent}
        try:
            r = requests.get(page_url, headers=header)
            r.encoding = 'utf-8'
            return r.text
            r.close()
        except Exception as e:
            print(e)
        return None

    def download_tuji(self, file_url, file_name):
        print(file_name + '下载中。。。')
        urllib.request.urlretrieve(file_url, file_name, self._process_bar)

    def _process_bar(self, blocknum, blocksize, totalsize):
        fin_size = blocknum * blocksize
        status = '正在下载'
        end_str = '\r'
        sep = '/'
        pervent = int(20 * fin_size / totalsize)
        pervent_str = pervent * '>'
        if fin_size >= totalsize:
            end_str = '\n'
            status = '下载完成'
            fin_size = totalsize
        _info = '%s [%s] %s %s %s' % (status, pervent_str.ljust(20), self._format_size(fin_size), sep, self._format_size(totalsize))
        print(_info.ljust(50), end=end_str)

    def _format_size(self, bytes):
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
