'''
Created on 2018��2��24��

@author: Joe
'''
#coding:utf-8
import re
import urlparse
from bs4 import BeautifulSoup, soup

class HtmlParser():

    def parser(self, page_url, html_cont):
        '''���ڽ�����ҳ���ݣ���ȡURL������
        :param page_url:����ҳ���URL
        :param html_cont:���ص���ҳ����
        :return:����URL������
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='urf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    def _get_new_urls(self, page_url, soup):
        '''��ȡ�µ�URl����
        :param page_url:����ҳ���url
        :param soup:soup
        :return:�����µ�Url����
        '''
        new_urls = set()
        #��ȡ����Ҫ���a���
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            #��ȡhref����
            new_url = link['href']
            #ƴ�ӳ���������ַ
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        '''��ȡ��Ч����
        :param page_url:����ҳ���URL
        :param soup:
        :return:������Ч����
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        #��ȡtag�а����������ı����ݣ���������tag�е����ݣ����������ΪUnicode�ַ�������
        data['summary'] = summary.get_text()
        return data