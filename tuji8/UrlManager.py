# -*- coding: utf-8 -*-

class UrlManager:

    def __init__(self):
        self.new_urls = []#未爬取的Url列表
        self.old_urls = []#已爬取的Url列表

    def has_new_url(self):
        '''
        判断是否有未爬取的Url
        :return:
        '''
        return self.new_url_size()!=0

    def get_new_url(self):
        '''
        获取一个未爬取的Url
        :return:
        '''
        new_url = self.new_urls.pop(0)
        self.old_urls.append(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        将新的Url添加到未爬取的Url集合中
        :param url:单个url
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.extend(url)

    def add_new_urls(self, urls):
        '''
        将新的Url添加到未爬取的Url集合中
        :param urls:url集合
        :return:
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.new_urls += urls

    def new_url_size(self):
        '''
        获取未爬取的Url集合的大小
        :return:
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        获取已经爬取的Url集合的大小
        :return:
        '''
        return len(self.old_urls)
