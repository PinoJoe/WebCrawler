'''
Created on 2018年2月24日

@author: Joe
'''
#coding:utf-8
class UrlManager():
    def __init__(self):
        self.new_urls = set()#未爬去的URL集合
        self.old_urls = set()#已爬取的URL集合

    def has_new_url(self):
        '''判断是否有未爬取的URL
        :return:
        '''
        return self.new_urls_size()!=0
    
    def get_new_url(self):
        '''获取一个未爬取的URL
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    def add_new_url(self, url):
        '''将新的URL添加到未爬取的URl集合中
        :param url:单个URl
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
    def new_url_size(self):
        '''获取未爬取URL集合的大小
        :return:
        '''
        return len(self.new_urls)
    
    def old_url_size(self):
        '''获取已经爬取URL集合的大小
        :return:
        '''
        return len(self.old_urls)