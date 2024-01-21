import requests
import os


class ApiCalls:
    def __init__(self, lat=43.8668, lon=-79.2663):
        self.api_key = os.environ.get("OWM_API_KEY")
        self.lon = lon
        self.lat = lat
        self.url = f"https://api.openweathermap.org/data/3.0/onecall"
   
        self.params = {
            "lat" : self.lat,
            "lon" : self.lon,
            "appid" : self.api_key,
            "exclude" : "current,daily,minutely"
        }


    def get_data(self):
        self.response = requests.get(url=self.url,params=self.params)
        self.response.raise_for_status()
        self.json_data = self.response.json()