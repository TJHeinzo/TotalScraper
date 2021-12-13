# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class TotalscraperPipeline:

    """
    def open_spider(self, spider):
        myFile = open('totalWine_items.csv', 'w')
        fieldNames = ['name', 'size', 'price', 'url']
        self.csv_writer = csv.DictWriter(myFile, fieldnames=fieldNames)
        csv_writer.writeheader()

    def close_spider(self, spider):
        return None
    """

    def process_item(self, item, spider):
        item["name"] = self.trimYear(item["name"])
        item["price"] = self.processPrice(item["price"])
        return item

    # Removes the vintage from a wines name if it has one
    def trimYear(self, name):
        if "," in name:
            return name[: name.index(",")]
        else:
            return name

    def processPrice(self, price):
        price = price.replace(",", "")
        return price.replace("$", "")
