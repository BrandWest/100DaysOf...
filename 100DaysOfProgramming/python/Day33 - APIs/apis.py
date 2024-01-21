'''
    APIs are: a set of functions, objects, protocols, and commands    
'''
import requests
import json
import datetime as dt

MY_LAT = 43.874168
MY_LONG = -79.258743
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=url)
response.raise_for_status()

#Gets the json data
json_response = response.json()
#print(response.status_code)

# print(json_response["iss_position"]["longitude"])
longitude = str(json_response["iss_position"]["longitude"])
latitude = str(json_response["iss_position"]["latitude"])
iss_position = (longitude, latitude)
# #Response Codes
# '''
#     1xx: Trying to find somehting (wait)
#     2xx: Successful request
#     3xx: No permissions
#     4xx: user error
#     5xx: server error
# '''

# geolocation_url = "https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}"
# url_encoded = geolocation_url.format(longitude=longitude, latitude=latitude)
# print(url_encoded)
# geolocation_response = requests.get(url=url_encoded)
# print(geolocation_response.status_code)

# json_geolocation_response = geolocation_response.json()
# print(json_geolocation_response)


'''
    api parameters
        Can be passed to APIs
'''
now = dt.datetime.now()


url ="https://api.sunrise-sunset.org/json"
params = {
    'lat': MY_LAT, 
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(url=url, params=params)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(now.hour, sunrise, sunset)