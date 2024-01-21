'''
    HTTP Post requests
        We give the data (not interested in the response.)
        requests.post()
    HTTP GET
        Get information
        requests.get(parameters)

    HTTP PUT
        Updating data in the external server (update values)
        requests.put()
    HTTP Delete
        Remove a peice of data
        requests.delete()
'''

import requests
import datetime as dt

def create_user():
    '''
        Creating a user
    '''

    user_params = {
        "token" : "D*9V<Cv-F:v4^NfJc]D(@'*U$_D]o:",
        "username" : "pvtcaboose",
        "agreeTermsOfService" : "yes",
        "notMinor" : "yes"
    }
    response = requests.post(url=tld, json=user_params)
    print(response.json())

def create_graph():
    endpoint = "v1/users/pvtcaboose/graphs"
    url = f"{tld}{endpoint}"
    headers = {
        "X-USER-TOKEN" : "D*9V<Cv-F:v4^NfJc]D(@'*U$_D]o:",
    }
    user_params = {
        "id" : "test-graph",
        "name" : "the-graphs-name",
        "unit" : "commit",
        "type" : "int",
        "color" : "kuro"
    }
    response = requests.post(url=url, headers=headers, json=user_params)
    print(response.json())

def add_graph_data():
    todays_date = dt.datetime.today().date().strftime("%Y%m%d") #''' USEFUL FOR THE DATE FORMATTING'''
    endpoint = "v1/users/pvtcaboose/graphs/test-graph"
    url = f"{tld}{endpoint}"
    headers = {
        "X-USER-TOKEN" : api_key
    }

    params = {
        "date" : todays_date,
        "quantity" : "5"
    }

    response = requests.post(url=url, headers=headers, json=params)


def delete_graph_data():
    endpoint = f"v1/users/{username}/graphs/{graph_id}/{dt.datetime.today().date().strftime('%Y%m%d')}"
    url = f"{tld}{endpoint}"

    headers = {
        "X-USER-TOKEN" : api_key
    }

    response = requests.delete(url=url, headers=headers)
    print(response)


def update_graph_data():
    endpoint = f"v1/users/{username}/graphs/{graph_id}/{dt.datetime.today().date().strftime('%Y%m%d')}"
    url = f"{tld}{endpoint}"
    headers = {
        "X-USER-TOKEN" : api_key
    }
    params = {
        "quantity" : "25"
    }

    response = requests.put(url=url, headers=headers, json=params)
    print(response)

if __name__ == "__main__":
    tld = "https://pixe.la/"
    api_key = "D*9V<Cv-F:v4^NfJc]D(@'*U$_D]o:"
    graph_id = "test-graph"
    username = "pvtcaboose"

    
    # create_user()
    # create_graph()
    # add_graph_data()
    # update_graph_data()
    delete_graph_data()