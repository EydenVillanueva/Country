import scrapy
from scrapy.loader import ItemLoader
from Example.items import MovieItem

class Movies(scrapy.Spider):

    name = "movies"
    allowed_domains = ["themoviedb.org"]
    start_urls = ['https://www.themoviedb.org/movie?language=en-EU&page=1',]

    def parse(self,response):

        movieItem = MovieItem()

        for movie in response.css('div.item'):
            movieItem['title'] = movie.css('div.wrapper div.flex a::text').get()
            movieItem['date'] = movie.css('div.wrapper span::text').get()
            movieItem['description'] = movie.css('p.overview::text').get()

            yield movieItem
            


