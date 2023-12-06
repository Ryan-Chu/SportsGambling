
import scrapy

class Selectors():
    def __init__(self, Site, Sport, Odds, Subject, Bet):
        self.Site = Site
        self.Sport = Sport
        self.Odds = Odds
        #Subject is the player or team
        self.Subject = Subject
        #Bet is the actual goal needed
        self.Bet = Bet

#Odds are for MoneyLine only
class GamblingItem(scrapy.Item):
    Site = scrapy.Field()
    Sport = scrapy.Field()
    Odds = scrapy.Field()
    #Subject is a player/team bet is on
    Subject = scrapy.Field()
    #Bet = what the player has to accomplish
    Bet = scrapy.Field()

