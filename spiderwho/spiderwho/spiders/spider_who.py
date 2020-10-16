import  scrapy

from ..items import WhoItem


class SpiderWho(scrapy.Spider):
    name = 'spiderwho'
    start_urls = ['https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/q-a-coronaviruses']

    def parse(self, response):
        items = WhoItem()
        all_div = response.css('.sf-accordion__panel')

        for panel in all_div:
            question = panel.css('.sf-accordion__link::text').extract_first()
            response = panel.css('.sf-accordion__content p:nth-child(2)::text').extract_first()
            # tag=panel.css('.tag::text').extract()

            items['question'] = question
            items['response'] = response
            # items['tag'] = tag
            yield items
