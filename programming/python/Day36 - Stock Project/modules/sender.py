import os
# from modules.stocks import Stocks

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

class Sender:
    def __init__(self, stock, articles):
        self.stock = stock
        self.articles = articles
        # self.proxy_client = TwilioHttpClient()
        # self.proxy_client.session.proxies = {"https": os.environ['https_proxy']}

        self.account_sid = os.environ.get("TWILIO_API_KEY")
        self.auth_token = os.environ.get("TWILIO_AUTH_KEY")

        self.from_ = "+13156673844"
        self.to_ = os.environ.get("TWILIO_TO")
        self.body_ : str

        # self.client = Client(self.account_sid, self.auth_token)
        # self.client = Client(self.account_sid, self.auth_token, http_client=self.proxy_client)
        # self.client = Client(self.account_sid, self.auth_token)


    def send_message(self):
        self.message = self.client.messages.create(
            from_=self.from_,
            body=self.body_,
            to=self.to_
        )
    
    def get_status(self):
        return self.message.status
    
    def format_message(self):
        body_ = ""
        for article in self.articles:
            print("===============================================")
            print(article)
            print("===============================================")
            if self.stock.fluctuation_pecentage > 2:
                body_ += f"\n{self.stock.stock}: {self.stock.up}\nHeadline: {article['title']}\nBreif: {article['description']}\nURL: {article['url']}\n"
            else:
                body_ += f"\n{self.stock.stock}: {self.stock.down}\nHeadline: {article['title']}\nBreif: {article['description']}\nURL: {article['url']}\n"
        self.body_ = body_
