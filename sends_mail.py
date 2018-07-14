import payments
from nameko.events import event_handler
import requests

class SendsMail:

    name = "sends_mail"

    @event_handler("payments", "payment_received")
    def handle_event(self, payload):
        print("payment received:", payload)
        return requests.post(
            "https://api.mailgun.net/v3/sandbox755e3e3d474a4b218e031f7213467c79.mailgun.org/messages",
            auth=("api", "7f0ee52f26f4a4ef8328e1195556c961-8b7bf2f1-1a549565"),
            data={"from": "jessicastenning@gmail.com",
                "to": "jessicalstenning@gmail.com",
                "subject": "Payment received",
                "text":   ("Dear {}, "
                "You have received a payment of {} {} "
                "from {} ({}). "
                "Yours, "
                "Student.com ").format((payload['payee']['name']), (payload['payment']['amount']),
                (payload['payment']['currency']), (payload['client']['name']),
                (payload['client']['email']))})
