# -*- coding: utf-8 -*-

import time
import HtmlDownloader
import HtmlParser
import DataOutput
import re

class SpiderMan:
    def __init__(self):
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.output = DataOutput.DataOutput()

    def crawl(self, root_url):
        content = self.downloader.download(root_url)
        urls = self.parser.parser_url(root_url, content)
        #构造一个获取评分和票房的连接，类似
        #http://service.library.mtime.com/Movie.api?
        # Ajax_CallBack=true
        # &Ajax_CallBackType=Mtime.Library.Services
        # &Ajax_CallBackMethod=GetMovieOverviewRating
        # &Ajax_CrossDomain=1
        # &Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F108737%2F
        # &t=2018 04 23 22 32 49 3282
        # &Ajax_CallBackArgument0=108737
        for url in urls:
            try:
                t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                rank_url = 'http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequesUrl=%s&t=%s&Ajax_CallBackArgument0=%s'%(url[0], t, url[1])
                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url, rank_content)
                self.output.store_data(data)
            except Exception as e:
                print(e, "Crawl failed")
        self.output.output_end()
        print("Crawl finish")

if __name__=='__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Shandong_Province_Jining/')
