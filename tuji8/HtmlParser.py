# -*- coding: utf-8 -*-

from lxml import etree

class HtmlParser:

    def get_source_urls(self, root_html):
        if root_html is None:
            return
        soup = etree.HTML(root_html)
        new_urls = soup.xpath("//*[@id='wrapper']//*[@class='con']/ul/li/a/@href")
        new_titles = soup.xpath("//*[@id='wrapper']//*[@class='con']/ul/li/a/@title")
        return new_urls, new_titles

    def get_middleware_url(self, source_url, source_html):
        if source_url is None or source_html is None:
            return 'get source_url failed'
        soup = etree.HTML(source_html)
        middleware_url = soup.xpath("//a[@rel='external nofollow']/@href")[1]
        return middleware_url

    def get_download_url(self, middleware_url, download_html):
        if middleware_url is None or download_html is None:
            return 'get middleware_url failed'
        soup = etree.HTML(download_html)
        download_url = soup.xpath("//a[@rel='external nofollow']/@href")[0]
        return download_url
