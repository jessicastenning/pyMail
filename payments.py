from faker import Factory

from nameko.events import EventDispatcher, event_handler
from nameko.timer import timer
import requests

fake = Factory.create()

payment_details = {}

class PaymentService(object):
    name = "payments"

    dispatch = EventDispatcher()

    @timer(interval=10)
    def emit_event(self):

        payload = {
            'client': {
                'name': fake.name(),
                'email': fake.safe_email()
            },
            'payee': {
                'name': fake.name(),
                'email': fake.safe_email()
            },
            'payment': {
                'amount': fake.random_int(),
                'currency': fake.random_element(
                    ("USD", "GBP", "EUR")
                )
            }
        }
        self.dispatch("payment_received", payload)
