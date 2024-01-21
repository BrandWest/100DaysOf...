import datetime as dt
#time.year, time.month, time.day, time.hour, time.minute, time.second
class WeatherData:
    def __init__(self, time, hour_weather):
        self.day = f"{time.year}-{time.month}-{time.day}"
        self.hour = time.hour
        self.weather_hour_data = hour_weather
