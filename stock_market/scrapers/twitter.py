from Scweet.scweet import scrape

class TwitterScraper:
    def __init__(self, words , from_date, until , interval):
        self.words = words
        self.from_date = from_date
        self.until = until
        self.interval = interval
    
    def scrape_tweets(self):
        data = scrape(words=self.words, since=self.from_date, until=self.until, interval=self.interval)
        return data