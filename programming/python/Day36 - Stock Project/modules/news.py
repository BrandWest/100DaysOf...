import requests

from modules.stocks import Stocks


class News:
    def __init__(self, stock):
        self.stock = stock
        self.api_key = "c4e5f1cf943e476884187e0da234e907"
        self.headline : str
        self.summary : str
        self.url = "https://newsapi.org/v2/everything"
        # self.url = "https://newsapi.org/v2/top-headlines"
        # print(stock.todays_date)
        self.params = {
            "q": stock.stock,
            "from" : str(stock.todays_date),
            "sortBy" : "popularity",
            "apiKey" : self.api_key
        }
        self.articles = {}
        

    def get_news(self):
        self.response = requests.get(url=self.url, params=self.params)
        print(self.response)
        self.data = self.response.json()
        if self.data["status"] == "ok":
            self.articles = self.data["articles"][:3]
            