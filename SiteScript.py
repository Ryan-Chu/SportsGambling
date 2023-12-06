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
#All soccer odds are for EPL Moneylines only
#All Basketball odds are for NBA Moneylines only

class FanduelSpider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'Fanduel.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(FanduelSpider, self).__init__(*args, **kwargs)
        #Site for basketball and soccer is the same, only different selectors
        if Sport == "Basketball":
            site = "https://sportsbook.fanduel.com/"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "https://sportsbook.fanduel.com/"
            self.start_urls = [site]
        else:
            raise Exception("Only Basketball and Soccer currently supported")

    def parse(self, response):
        Item = GamblingItem()
        #check this self.sport
        if self.Sport == "Basketball":
            FanduelbbSelector= Selectors("https://sportsbook.fanduel.com/", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

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
            site = "https://sportsbook.draftkings.com/leagues/basketball/nba"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "https://sportsbook.draftkings.com/leagues/soccer/england---premier-league"
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
            site = "https://sports.az.betmgm.com/en/sports/soccer-4"
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

class DraftkingsSpider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'Draftkings.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(DraftkingsSpider, self).__init__(*args, **kwargs)
        if Sport == "Basketball":
            site = "https://sportsbook.draftkings.com/leagues/basketball/nba"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "https://sportsbook.draftkings.com/leagues/soccer/england---premier-league"
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





class Betusspider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'Betus.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(Betusspider, self).__init__(*args, **kwargs)
        if Sport == "Basketball":
            site = "https://www.betus.com.pa/sportsbook/nba/"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "https://www.betus.com.pa/sportsbook/england-premier-league/"
            self.start_urls = [site]
        else:
            raise Exception("Only Basketball and Soccer currently supported")

    def parse(self, response):
        Item = GamblingItem()
        #check this self.sport
        if self.Sport == "Basketball":
            BetusbbSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = BetusbbSelector.Site
            Item.Sport = BetusbbSelector.Sport
            Item.Odds = BetusbbSelector.Odds
            Item.Subject = BetusbbSelector.Subject
            Item.Bet = BetusbbSelector.Bet
        elif self.sport == "Soccer":
            BetussSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = BetussSelector.Site
            Item.Sport = BetussSelector.Sport
            Item.Odds = BetussSelector.Odds
            Item.Subject = BetussSelector.Subject
            Item.Bet = BetussSelector.Bet
        yield Item

    pass

class Bovadaspider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'Betus.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(Bovadaspider, self).__init__(*args, **kwargs)
        if Sport == "Basketball":
            site = "https://www.bovada.lv/sports/basketball/nba"
            self.start_urls = [site]
        elif Sport == "Soccer":
            site = "https://www.bovada.lv/sports/soccer/europe/england/premier-league"
            self.start_urls = [site]
        else:
            raise Exception("Only Basketball and Soccer currently supported")

    def parse(self, response):
        Item = GamblingItem()
        #check this self.sport
        if self.Sport == "Basketball":
            BovadabbSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = BovadabbSelector.Site
            Item.Sport = BovadabbSelector.Sport
            Item.Odds = BovadabbSelector.Odds
            Item.Subject = BovadabbSelector.Subject
            Item.Bet = BovadabbSelector.Bet
        elif self.sport == "Soccer":
            BovadasSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = BovadasSelector.Site
            Item.Sport = BovadasSelector.Sport
            Item.Odds = BovadasSelector.Odds
            Item.Subject = BovadasSelector.Subject
            Item.Bet = BovadasSelector.Bet
        yield Item

    pass

class Yahoospider(scrapy.Spider):

    custom_settings = {
        'FEEDS': { 'Betus.csv': { 'format': 'csv',}}
    }

    def __init__(self, Sport=None, *args, **kwargs):
        super(Yahoospider, self).__init__(*args, **kwargs)
        if Sport == "Basketball":
            site = "https://sports.yahoo.com/nba/odds/"
            self.start_urls = [site]
        elif Sport == "Soccer":
            #Yahoo doesn't have different url for epl vs soccer
            site = "https://sports.yahoo.com/soccer/odds/"
            self.start_urls = [site]
        else:
            raise Exception("Only Basketball and Soccer currently supported")

    def parse(self, response):
        Item = GamblingItem()
        #check this self.sport
        if self.Sport == "Basketball":
            YahoobbSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = YahoobbSelector.Site
            Item.Sport = YahoobbSelector.Sport
            Item.Odds = YahoobbSelector.Odds
            Item.Subject = YahoobbSelector.Subject
            Item.Bet = YahoobbSelector.Bet
        elif self.sport == "Soccer":
            YahoosSelector= Selectors("Site selector", "Sport selector", "Odds selector", "Subject selector", "Bets selector")

            Item.Site = YahoosSelector.Site
            Item.Sport = YahoosSelector.Sport
            Item.Odds = YahoosSelector.Odds
            Item.Subject = YahoosSelector.Subject
            Item.Bet = YahoosSelector.Bet
        yield Item

    pass

#main script to iterate through
Spiderlist = [FanduelSpider, DraftkingsSpider, MGMspider, Betusspider, Bovadaspider, Yahoospider]
#for x in range(Spiderlist.len()):
#process.crawl(x)
#process.start()
