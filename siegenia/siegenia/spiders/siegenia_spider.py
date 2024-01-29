import scrapy
from bs4 import BeautifulSoup


class SiegeniaSpider(scrapy.Spider):
    name = "siegenia_spider"
    allowed_domains = ["shop.siegenia.com"]

    def start_requests(self):
        base_url = "https://shop.siegenia.com/siegenia/de/search?q=*&page={}&viewType=resultsOnly"  # noqa
        # Start from page 0
        page_number = 0
        start_url = base_url.format(page_number)

        yield scrapy.Request(
            url=start_url, callback=self.parse, meta={"page_number": page_number}
        )

    def parse(self, response):
        # check if the result holds any data
        if not response.text:
            return

        page_number = response.meta["page_number"]
        soup = BeautifulSoup(response.text, "html.parser")
        product_teasers = soup.find_all("div", class_="product-teaser")

        for product_teaser in product_teasers:
            product_data = {
                "name": product_teaser.find(
                    "span", class_="product-teaser__title"
                ).text.strip(),
                "sku": product_teaser.find(
                    "span", class_="product-teaser__sku"
                ).text.strip(),
                "price": product_teaser.find("span", class_="value").text.strip(),
                "url": response.urljoin(
                    product_teaser.find("a", class_="product-teaser__link")["href"]
                ),
            }

            yield product_data

        next_page_number = page_number + 1
        next_page_url = "https://shop.siegenia.com/siegenia/de/search?q=*&page={}&viewType=resultsOnly".format(  # noqa
            next_page_number
        )
        yield scrapy.Request(
            url=next_page_url,
            callback=self.parse,
            meta={"page_number": next_page_number},
        )
