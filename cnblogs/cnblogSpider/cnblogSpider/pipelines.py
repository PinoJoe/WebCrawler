# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
class CnblogspiderPipeline(object):
    def __init__(self):
        self.file = open('papers.json', 'wb')
    def process_item(self, item, spider):
        if item['title']:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line.encode())
            return item
        else:
            raise DropItem("Missing title in %s" % item)

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['cimage_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
