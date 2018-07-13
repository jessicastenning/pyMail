from faker import Factory
from sends_messages import send_simple_message

from nameko.events import EventDispatcher, event_handler
from nameko.timer import timer

fake = Factory.create()

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
