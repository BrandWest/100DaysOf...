import requests
import datetime as dt


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.stock}&apikey={self.api_key}
class Stocks:
    def __init__(self, stock=STOCK, company=COMPANY_NAME, percentage_window=5):
        self.api_key = "LYOY14FC69MEU5G4"
        self.url="https://www.alphavantage.co/query"
        self.stock = stock
        self.company = company
        self.todays_date = dt.datetime.today().replace(day=dt.datetime.today().day-1)
        self.todays_price : float
        self.previous_date : str
        self.previous_price : float
        self.fluctuation_percentage: int
        self.fluctuation_dollas: float
        self.up = "📈"
        self.down = "📉"
        self.params = {
            "function" : "TIME_SERIES_DAILY_ADJUSTED",
            "symbol" : {self.stock},
            "apikey" : {self.api_key}
        }
        self.percentage_window = percentage_window

    def get_stock_info(self):
        response = requests.get(url=self.url, params=self.params)
        self.response = response.json()["Time Series (Daily)"]


    def set_stock_info(self):
        self.todays_price = float(self.response[str(self.todays_date)]["4. close"])
        self.previous_price = float(self.response[str(self.previous_date)]["4. close"])
        self.fluctuation_pecentage = 100 * ((self.previous_price - self.todays_price) / self.previous_price)
        self.fluctuation_dollas = self.previous_price - self.todays_price

    def set_dates(self):
        self.todays_date = dt.datetime.today().replace(day=dt.datetime.today().day-1)
        
        if self.todays_date.weekday() < 5:
            self.previous_date = self.todays_date
            if self.previous_date.weekday() == 5:
                self.previous_date = self.todays_date.replace(day=self.todays_date.day-1).date()
            elif self.previous_date.weekday() == 6:
                self.previous_date = self.todays_date.replace(day=self.todays_date.day-2).date()
            else:
                self.previous_date = self.todays_date.replace(day=self.todays_date.day-1).date()
            self.todays_date = self.todays_date.date()
        else:
            print("No trading on the weekend.")
    