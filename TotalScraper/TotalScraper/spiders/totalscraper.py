import scrapy


class TotalScraper(scrapy.Spider):
    name = "total"
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    start_urls = [
        "https://www.totalwine.com/wine/c/c0020?viewall=true&pageSize=120&aty=1,1,0,0&instock=1"
    ]
    pageNum = 1

    def parse(self, response):
        for product in response.css("article.productCard__2nWxIKmi"):
            yield {
                "name": product.xpath(".//h2/a/text()").get(),
                "size": product.xpath(".//h2/span/text()").get(),
                "price": product.xpath('.//*[@class="price__1JvDDp_x"]/text()').get(),
                # "isWD": 0 if product.xpath('.//div[@class="Popoverstyled__ToolTipHolder-shared-packages__sc-16w01om-0 aycRH"]').get() is None else 1,
                "url": "https://www.totalwine.com"
                + product.xpath(".//h2/a/@href").get(),
            }

        maxPage = int(
            response.css('a[data-at="product-search-pagination-link"]::text').getall()[
                -1
            ]
        )

        self.pageNum += 1
        if self.pageNum <= maxPage:
            yield response.follow(
                f"https://www.totalwine.com/wine/c/c0020?viewall=true&page={self.pageNum}&pageSize=120&aty=1,1,0,0&instock=1",
                callback=self.parse,
            )
