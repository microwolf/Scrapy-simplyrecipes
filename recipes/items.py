# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    dish = scrapy.Field()
    rating_num = scrapy.Field()
    rating_star = scrapy.Field()
    num_comment = scrapy.Field()
    tags = scrapy.Field()
    meta_description = scrapy.Field()

    time_prep = scrapy.Field()
    time_cook = scrapy.Field()
    time_other_type = scrapy.Field()
    time_other = scrapy.Field()
    time_other_full = scrapy.Field()

    servings = scrapy.Field()
    ingredients = scrapy.Field()
    cook_type = scrapy.Field()
    
    


