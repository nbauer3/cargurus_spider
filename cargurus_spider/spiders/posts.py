# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    #for i in range(10):
    allowed_domains = [
	    'www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164#resultsPage=1',
	    #'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164#resultsPage=2', 
	]
    start_urls = [
	    'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164#resultsPage=5',
	    #'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164#resultsPage=2', 
	]


    # TODO yield data to MySql or .json or .csv file

    # didnt work, can only retrieve page 1 data - updates initial page visit to be page #1
    def parse(self, response):
    	# TODO PAGE CHANGES WITH THIS SO MAYBE LOOPAND APPEND URL?
    	#
    	url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164#resultsPage=5' #+ str(i)
    	yield scrapy.Request(url=url, callback=self.parse)
    	self.scrape(response)

    	# A @href element that refers to the 'next button'
    	#response.xpath('//*[@id="mainSearchResultsContainer"]/div[1]/div[1]/a[3]/@href').extract_first()
    	

    def scrape(self, response):
    	title_0 = response.xpath('//h1/text()').extract()[0]
    	title_1 = response.xpath('//h1/em/text()').extract()[0]
    	title_2 = response.xpath('//h1/text()').extract()[1]
    	title_3 = response.xpath('//h1/em[2]/text()').extract()[0]

    	title = title_0 + title_1 + title_2 + str(title_3)

    	print '\n\n#################### - STARTING SPIDER - ####################\n\n'
        print title

    	# extra data listing - 'Used Cars'
        posts = response.xpath('//*[@class="cg-dealFinder-result-model"]')
        i = 0
        j = 0

        # yielding data for .json will be out of order bc its presented in a terrible fashion#str()?
            #yield {
            #    'Post Title': postTitle,
            #    'Price': price,
            #    'Mileage': mileage,
            #}

        #45 bc there are 45 /spans
        while i < 45:
        	# some funky code
        	info = response.xpath('.//*[@class="cg-dealFinder-result-model"]/span/text()').extract()[i]
        	if i % 3 == 0:
        		# used cars is at position 2/3 for all 15 posts

        		# the deal over or under is on the car is 2/3
        		# great/good/bad deals with $ amount over/under market price
        		# response.xpath('.//*[@class="cg-dealFinder-result-deal"]/div/text()').extract()
        		
        		price = response.xpath('//*[@class="cg-dealFinder-result-stats"]/p/span/text()').extract()[j]
        		mileage = response.xpath('.//*[@class="cg-dealFinder-result-stats"]/p[2]/span/text()').extract()[j]
        		j += 1
        		print '\n-------------------------------------------------------------\n'
        		print 'Post #' + str(1 + (i/3)) # LOL
        		if i % 2 == 0:
        			print 'Price: ' + str(price)
        		else:
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
     	#yield scrapy.Request('https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2207&zip=20164#resultsPage=2')