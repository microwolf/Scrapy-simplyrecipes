from recipes.items import RecipesItem
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess

class RecipesSpider(Spider):
    name = "recipes_spider"
    allowed_urls = ["https://www.simplyrecipes.com/"]
    #start_urls = ["https://www.simplyrecipes.com/recipes/course/dinner/", "https://www.simplyrecipes.com/recipes/course/stew/", "https://www.simplyrecipes.com/recipes/course/soup/"]
    start_urls = ["https://www.simplyrecipes.com/recipes/course/dinner/"]
    
    def parse(self, response):
        num_pages = int(response.xpath('//a[@class="rpg-page-numbers"]/text()').extract()[-1])
        #num_pages = 2
        #page_lst = [f'https://www.simplyrecipes.com/recipes/course/dinner/page/{i+1}/' for i in range(num_pages)]
        page_lst = [f'https://www.simplyrecipes.com/recipes/course/soup/page/{i+1}/' for i in range(num_pages)]

        for page in page_lst:
            yield Request(url = page, callback = self.parse_recipe_lst_page)

    def parse_recipe_lst_page(self, response):
        recipe_urls = response.xpath('//a[@itemprop="url"]/@href').extract()

        for url in recipe_urls:
            yield Request(url = url, callback = self.parse_recipe_page)

    def parse_recipe_page(self, response):
        # basic dish info
        author = response.xpath('//a[@rel="author"]//text()').extract_first()
        dish = response.xpath('//h1[@class="entry-title"]/text()').extract()
        rating_num = response.xpath('//span[@class="total-count ratings"]/text()').extract_first()
        rating_star = response.xpath('//span[@class="rating-value"]/text()').extract_first()
        #comment_num = response.xpath('//span[@class="total-count comments"]/text()').extract_first()
        tags = response.xpath('//span[@class="primary-terms-container"]//span/text()').extract()
        meta_description = response.xpath('//div[@class="meta-description-content"]/text()').extract_first()
        # cooking time
        time_prep = response.xpath('//span[@class="preptime"]/text()').extract_first()
        time_cook = response.xpath('//span[@class="cooktime"]/text()').extract_first()
        #time_other_type = response.xpath('//li[@class="recipe-other"]//text()').extract()[0]
        #time_other = response.xpath('//li[@class="recipe-other"]//text()').extract()[-1]
        try:
            time_other_full = response.xpath('//li[@class="recipe-other"]//text()').extract()
        except Exception as e:
            print(type(e), e)
            pass
        # cooking info
        servings = response.xpath('//span[@class="yield"]//text()').extract_first()
        ingredients = response.xpath('//li[@class="ingredient"]/text()').extract()

        item = RecipesItem()

        #item['cook_type'] = 'dinner'
        item['author'] = author
        item['dish'] = dish
        item['rating_num'] = rating_num 
        item['rating_star'] = rating_star
        #item['comment_num'] = comment_num
        item['tags'] = tags
        item['meta_description'] = meta_description

        item['time_prep'] = time_prep
        item['time_cook'] = time_cook
        #item['time_other_type'] = time_other_type
        #item['time_other'] = time_other
        item['time_other_full'] = time_other_full

        item['servings'] = servings
        item['ingredients'] = ingredients

        yield item
