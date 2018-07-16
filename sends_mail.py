from nameko.events import event_handler
from constants import API_KEY, EMAIL, DOMAIN
import payments
import requests

class SendsMail:

    name = "sends_mail"

    @event_handler("payments", "payment_received")
    def handle_event(self, payload):
        print("payment received:", payload)
        return requests.post(
            DOMAIN,
            auth=("api", API_KEY),
            data = self.format_response_func(payload))


    def format_response_func(self,payload):
            return {
                "from": EMAIL,
                "to": EMAIL,
                "subject": "Payment received",
                "text": ("""
                    Dear {},

                    You have received a payment of {} {} from {} ({}).

                    Yours,

                    Student.com
                    """).format(
                    (payload['payee']['name']),(payload['payment']['amount']),
                    (payload['payment']['currency']), (payload['client']['name']),
                    (payload['client']['email']))}
