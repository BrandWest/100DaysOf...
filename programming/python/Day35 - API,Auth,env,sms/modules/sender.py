import os

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

class Sender:
    def __init__(self):
        self.proxy_client = TwilioHttpClient()
        self.proxy_client.session.proxies = {"https": os.environ['https_proxy']}

        self.account_sid = os.environ.get("TWILIO_API_KEY")
        self.auth_token = os.environ.get("TWILIO_AUTH_KEY")

        self.from_ = "+13156673844"
        self.to_ = os.environ.get("TWILIO_TO")
        self.body_ : str

        self.client = Client(self.account_sid, self.auth_token)
        self.client = Client(self.account_sid, self.auth_token, http_client=self.proxy_client)

    def send_message(self):
        self.message = self.client.messages.create(
            from_=self.from_,
            body=self.body_,
            to=self.to_
        )
    
    def get_status(self):
        return self.message.status