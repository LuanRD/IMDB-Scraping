import scrapy
import re


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/toptv/']

    def parse(self, response):
        for i, series in enumerate(response.css('.titleColumn')):
            yield{
                'titulos': series.css('.titleColumn a::text').get(),
                'ano': series.css('.secondaryInfo::text').get()[1:-1],
                'nota': response.css('strong::text').getall()[i],
                'votes':re.search('<strong title="[0-9]\.[0-9] based on (.+?) user ratings">[0-9]\.[0-9]</strong>',
                                   response.css('strong').getall()[i]).group(1)}
        pass
