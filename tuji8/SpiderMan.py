# -*- coding: utf-8 -*-
import HtmlDownloader
import HtmlParser
import UrlManager
import string
from urllib.parse import quote
import time

class SpiderMan:
    def __init__(self):
        self.manager = UrlManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()

    def crawl(self, root_url):
        root_cont = self.downloader.download_page(root_url)
        new_urls, new_titles = self.parser.get_source_urls(root_cont)
        self.manager.add_new_urls(new_urls)
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                #根据顺序页面，获取本页所有图集名称及下载页面链接
                source_url = self.manager.get_new_url()
                file_name = new_titles.pop(0)
                source_html = self.downloader.download_page(source_url)
                middleware_url = self.parser.get_middleware_url(source_url, source_html)
                middleware_url = quote(middleware_url, safe=string.printable)
                print(middleware_url)
                while True:
                    try:
                        time.sleep(30)
                        download_html = self.downloader.download_page(middleware_url)
                        download_url = self.parser.get_download_url(middleware_url, download_html)
                        download_url = quote(download_url, safe=string.printable)
                    except Exception as e:
                        print(e)
                        download_html.close()
                while True:
                    try:
                        self.downloader.download_tuji(download_url, file_name)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)

if __name__=="__main__":
    spider_man = SpiderMan()
    root_url = "http://www.tuji8.com/tuji"
    spider_man.crawl(root_url)
    print ('finished')
