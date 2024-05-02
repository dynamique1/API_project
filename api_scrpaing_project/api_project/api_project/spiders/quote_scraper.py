import scrapy
import json


class QuoteScraperSpider(scrapy.Spider):
    name = "quote_scraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        json_response = json.loads(response.body)
        quotes = json_response.get('quotes')
        for quote in quotes:
            yield{
                'author':quote.get('author').get('name'),
                'tags':quote.get('tags'),
                'text':quote.get('text'),
            }

