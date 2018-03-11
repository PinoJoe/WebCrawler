'''
Created on 2018��2��24��

@author: Joe
'''
#coding:utf-8
class UrlManager():
    def __init__(self):
        self.new_urls = set()#δ��ȥ��URL����
        self.old_urls = set()#����ȡ��URL����

    def has_new_url(self):
        '''�ж��Ƿ���δ��ȡ��URL
        :return:
        '''
        return self.new_urls_size()!=0
    
    def get_new_url(self):
        '''��ȡһ��δ��ȡ��URL
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    def add_new_url(self, url):
        '''���µ�URL��ӵ�δ��ȡ��URl������
        :param url:����URl
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
    def new_url_size(self):
        '''��ȡδ��ȡURL���ϵĴ�С
        :return:
        '''
        return len(self.new_urls)
    
    def old_url_size(self):
        '''��ȡ�Ѿ���ȡURL���ϵĴ�С
        :return:
        '''
        return len(self.old_urls)