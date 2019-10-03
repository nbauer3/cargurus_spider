# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164']
    start_urls = ['http://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164/']

    def parse(self, response):
    	# returns for all cars: car listing - 'Used Cars' - location
    	# response.xpath('//*[@class="cg-dealFinder-result-model"]/span/text()').extract()
        posts = response.xpath('//*[@class="cg-dealFinder-result-model"]')
        i = 0
        for post in posts:
        	# some funky code print post #
        	info = response.xpath('.//*[@class="cg-dealFinder-result-model"]/span/text()').extract()[i]
        	if i % 3 == 0:
        		print 'Post #' + str(i/3)
        	print info
        	i += 1
