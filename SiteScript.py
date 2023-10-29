from typing import Iterable
import scrapy
from scrapy.http import Request
from items import *

'''
#Redo but with passing different spider classes not instances.
Spiderlist = []

SitesSelector = [FanduelBBSelector, DraftKingsBBSelector]
Sitesurl = [
            "https://sportsbook.fanduel.com/",
            "https://sportsbook.draftkings.com/?category=live-in-game&subcategory=basketball"
        ]

#Rewritten to not pass instance and pass class for .crawl()
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
    pass
'''

class FanduelSpider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'Fanduel.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(FanduelSpider, self).__init__(*args, **kwargs)
        if Sport == "Basketball":
            site = "https://sportsbook.fanduel.com/"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "soccer site for fanduel"
            self.start_urls = [site]
        else:
            raise Exception("Only Basketball and Soccer currently supported")

    def parse(self, response):
        Item = GamblingItem()
        #check this self.sport
        if self.Sport == "Basketball":
            FanduelbbSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = FanduelbbSelector.Site
            Item.Sport = FanduelbbSelector.Sport
            Item.Odds = FanduelbbSelector.Odds
            Item.Subject = FanduelbbSelector.Subject
            Item.Bet = FanduelbbSelector.Bet
        elif self.sport == "Soccer":
            FanduelsSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = FanduelsSelector.Site
            Item.Sport = FanduelsSelector.Sport
            Item.Odds = FanduelsSelector.Odds
            Item.Subject = FanduelsSelector.Subject
            Item.Bet = FanduelsSelector.Bet
        yield Item
    pass




class DraftkingsSpider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'Draftkings.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(DraftkingsSpider, self).__init__(*args, **kwargs)
        if Sport == "Basketball":
            site = "https://sportsbook.draftkings.com/?category=live-in-game&subcategory=basketball"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "Soccer site for draftkings"
            self.start_urls = [site]
        else:
            raise Exception("Only Basketball and Soccer currently supported")

    def parse(self, response):
        Item = GamblingItem()
        #check this self.sport
        if self.Sport == "Basketball":
            DraftKingsbbSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = DraftKingsbbSelector.Site
            Item.Sport = DraftKingsbbSelector.Sport
            Item.Odds = DraftKingsbbSelector.Odds
            Item.Subject = DraftKingsbbSelector.Subject
            Item.Bet = DraftKingsbbSelector.Bet
        elif self.sport == "Soccer":
            DraftKingssSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = DraftKingssSelector.Site
            Item.Sport = DraftKingssSelector.Sport
            Item.Odds = DraftKingssSelector.Odds
            Item.Subject = DraftKingssSelector.Subject
            Item.Bet = DraftKingssSelector.Bet
        yield Item

    pass





class MGMspider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'MGM.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(MGMspider, self).__init__(*args, **kwargs)
        if Sport == "Basketball":
            site = "https://sports.az.betmgm.com/en/sports/basketball-7"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "Soccer site for MGM"
            self.start_urls = [site]
        else:
            raise Exception("Only Basketball and Soccer currently supported")

    def parse(self, response):
        Item = GamblingItem()
        #check this self.sport
        if self.Sport == "Basketball":
            MGMbbSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = MGMbbSelector.Site
            Item.Sport = MGMbbSelector.Sport
            Item.Odds = MGMbbSelector.Odds
            Item.Subject = MGMbbSelector.Subject
            Item.Bet = MGMbbSelector.Bet
        elif self.sport == "Soccer":
            MGMsSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = MGMsSelector.Site
            Item.Sport = MGMsSelector.Sport
            Item.Odds = MGMsSelector.Odds
            Item.Subject = MGMsSelector.Subject
            Item.Bet = MGMsSelector.Bet
        yield Item

    pass


#main script to iterate through
Spiderlist = [FanduelSpider, DraftkingsSpider, MGMspider]
#for x in range(Spiderlist.len()):
#process.crawl(x)
#process.start()
