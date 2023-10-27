import scrapy

SitesURL = ["https://sportsbook.fanduel.com/", "https://sportsbook.draftkings.com/?category=live-in-game&subcategory=basketball", ""]
SitesSelector = ["Fanduel Selector", "DraftKings Selector"]

class SiteScript(scrapy.Spider):
    name = "SiteScript"
    start_urls = SitesURL
    