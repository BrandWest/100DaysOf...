from modules.api_calls import ApiCalls
from modules.day_data import WeatherData
from modules.sender import Sender
import datetime as dt


if __name__ == "__main__":
    api = ApiCalls()
    api.get_data()
    twilio = Sender()

    rain = False
    day_objects = []
    
    for index in api.json_data["hourly"]:
        time = dt.datetime.fromtimestamp(index["dt"])
        if time.day == dt.datetime.now().day and time.hour >= 6 and time.hour <= 19:
            weather = f"weather {time.hour}"
            weather = WeatherData(time=time, hour_weather=api.json_data["hourly"][time.hour])
            day_objects.append(weather)
    
    for weather in day_objects:
        for daily in weather.weather_hour_data["weather"]:
            if daily["id"] < 700:
                twilio.body_ = f"Its going to rain today starting at {weather.time}. Remeber to bring an ☂️"
                twilio.send_message()
                rain = True
                break
    
    if rain == False:
        twilio.body_ = "Its not going to rain today ☀️."
        twilio.send_message()


        