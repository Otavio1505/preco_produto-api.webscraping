import scrapy


class MlSpider(scrapy.Spider):
    name = 'ml'

    start_urls = [f'https://www.mercadolivre.com.br/ofertas?page=1']

    def parse(self, response,**kwargs):
        for i in response.xpath('//li[@class="promotion-item avg"]'):
            price = i.xpath('.//span[@class="promotion-item__price"]//text()').get()
            title = i.xpath('.//p[@class="promotion-item__title"]/text()').get()
            link = i.xpath('./a/@href\n').get()
            old_price = i.xpath('.//span[@class="promotion-item__oldprice"]//text()').getall()
        yield {
            'price': price,
            'title': title,
            'link': link,
            'old_price': old_price
        }
        next_page = response.xpath('//a[contains(@title,"Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
