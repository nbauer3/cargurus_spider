# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164']
    start_urls = ['http://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164/']

    def parse(self, response):
    	title_0 = response.xpath('//h1/text()').extract()[0]
    	title_1 = response.xpath('//h1/em/text()').extract()[0]
    	title_2 = response.xpath('//h1/text()').extract()[1]
    	title_3 = str(response.xpath('//h1/em[2]/text()').extract_first())
    	# title location coming back as 'Nationwide'
    	title = title_0 + title_1 + title_2 + title_3

    	print '\n\n#################### - STARTING SPIDER - ####################\n\n'
        print title

    	# returns for all cars: car listing - 'Used Cars' - location
    	# response.xpath('//*[@class="cg-dealFinder-result-model"]/span/text()').extract()
        posts = response.xpath('//*[@class="cg-dealFinder-result-model"]')
        i = 0
        j = 0

        #45 bc there are 45 /spans
        while i < 45:
        	# some funky code
        	info = response.xpath('.//*[@class="cg-dealFinder-result-model"]/span/text()').extract()[i]
        	if i % 3 == 0:
        		# used cars is at position 2/3 for all 15 posts
        		# the deal over or under is on the car is 2/3
        		# response.xpath('.//*[@class="cg-dealFinder-result-deal"]/div/text()').extract()
        		price = response.xpath('//*[@class="cg-dealFinder-result-stats"]/p/span/text()').extract()[j]
        		mileage = response.xpath('.//*[@class="cg-dealFinder-result-stats"]/p[2]/span/text()').extract()[j]
        		j += 1
        		print '\n-------------------------------------------------------------\n'
        		print 'Post #' + str(1 + (i/3)) # LOL
        		print 'Price: $' + str(price)
        		print 'Mileage: ' + str(mileage)
        	#attempting to get rid of Used Cars	
        	#if str(info) != 'Used Cars'
        	print info
        	i += 1

        print '\n\n##################### - ENDING SPIDER - #####################\n\n'
        #next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
     	#absolute_next_page_url = response.urljoin(next_page_url)
     	# doest work bc adds '/' but also hardcoded the url into scrapy.Request
     	# absolute_next_page_url = response.urljoin('#resultsPage=2')

     	# hard coding new url doesnt work
     	yield scrapy.Request('https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164#resultsPage=2')