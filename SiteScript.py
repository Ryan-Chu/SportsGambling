from typing import Iterable
import scrapy
from scrapy.http import Request
from items import *


# 1's are placeholder for xpath or css selector for url
FanduelSelector = Selectors(1, 1, 1, 1, 1)
DraftKingsSelector = Selectors(1, 1, 1, 1, 1)

SitesSelector = [FanduelSelector, DraftKingsSelector]
Sitesurl = [
            "https://sportsbook.fanduel.com/",
            "https://sportsbook.draftkings.com/?category=live-in-game&subcategory=basketball"
        ]

class SiteScript(scrapy.Spider):
    name = "SiteInfo"

    def __init__(self, site=None, *args, **kwargs):
        super(SiteScript, self).__init__(*args, **kwargs)
        self.start_urls = [Sitesurl[site]]
        self.selector = SitesSelector[site]

    def parse(self, response):
        item = GamblingItem()
        item.Site = self.selector[1]
        item.Sport = self.selector[2]
        item.Odds = self.selector[3]
        item.Subject = self.selector[4]
        item.Bet = self.selector[5]
        
        
        yield item


#main script iterates through sites and run spider on it