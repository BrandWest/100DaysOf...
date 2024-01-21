import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_url = "https://api.sheety.co/c0600a54c4a69fa054eec83059d2ab39/flightTracker/prices"
        self.post_url = "https://api.sheety.co/c0600a54c4a69fa054eec83059d2ab39/flightTracker/prices"
        self.put_url = "https://api.sheety.co/c0600a54c4a69fa054eec83059d2ab39/flightTracker/prices/"
        self.response = ""
        self.sheety_auth_key = "oUNhSRy5DTpg3yJrX_n"
        self.current_lowest_price : float
        self.iata_code : str
        self.city : str
        self.headers = {
            "Content-Type" : "application/json",
            "Authorization" : "Bearer oUNhSRy5DTpg3yJrX_n"
        }
        self.post_flight_data = {
            "price" : {
                "city" : str,
                "iataCode" : str,
                "lowestPrice" : float
            }
        }

        self.put_flight_data = {             
            "price" : {
                "lowestPrice" : float
            }
        }
        self.params = None

    #set the found data with the lowest price.
    def add_flight_data(self):        
        response_post = requests.post(url=self.post_url, headers=self.headers, json=self.post_flight_data)
        response_post.raise_for_status()

    #Get the flight data from the sheets
    def get_flight_data(self):
        get_response = requests.get(url=self.get_url, headers=self.headers, params=self.params)
        get_response.raise_for_status()
        self.response = get_response.json()
        
    
    #Filters the data 
    def filter_data(self, iataCode):
        self.params = f"filter[iataCode]={iataCode}"
        self.get_flight_data()
        print(self.response["prices"])
        self.id = self.response['prices'][0]['id']


    # Changes the current lowest price
    def change_lowest_price(self, new_price, iataCode):
        self.filter_data(iataCode)
        changes = {
            "price" : {
                "lowestPrice" : new_price
            }
        }

        self.put_url = f"{self.put_url}{self.id}"
        put_response = requests.put(url=self.put_url, headers=self.headers, json=changes)
        put_response.raise_for_status()
