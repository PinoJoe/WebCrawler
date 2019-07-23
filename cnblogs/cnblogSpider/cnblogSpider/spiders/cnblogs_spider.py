# coding:utf-8
import scrapy
from cnblogSpider.items import CnblogspiderItem
class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"# 爬虫的名字
    allowed_domains = ["cnblogs.com"]# 允许的域名
    start_urls = [
            "https://www.cnblogs.com/pythonista/default.html?page=1"
    ]
    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章
        papers = response.xpath(".//*[@class='day']")
        # 从每篇文章中抽取数据
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            item = CnblogspiderItem(url=url, title=title, time=time, content=content)
            yield item
        next_page = scrapy.Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)
