from nameko.events import event_handler
import payments
import requests

class SendsMail:

    name = "sends_mail"

    @event_handler("payments", "payment_received")
    def handle_event(self, payload):
        print("payment received:", payload)
        return requests.post(
            "https://api.mailgun.net/v3/sandbox755e3e3d474a4b218e031f7213467c79.mailgun.org/messages",
            auth=("api", "5ff5b93ffdea5568338776eaf366f060-8b7bf2f1-17f4b7c0"),
            data = self.format_response_func(payload))


    def format_response_func(self,payload):
            return {
                "from": "jessicalstenning@gmail.com",
                "to": "jessicalstenning@gmail.com",
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
