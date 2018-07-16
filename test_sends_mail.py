from nameko.testing.services import worker_factory
import requests
from mock import patch, Mock
from sends_mail import SendsMail


@patch('requests.post')
def test_handle_event_calls_requests_post_with_correct_data(mock_requests_post):

    mockresponse = Mock()
    mock_requests_post.return_value = mockresponse

    service = worker_factory(SendsMail)

    mock_payload = {
        'client': { 'name': 'mock_name', 'email': 'mock_email' },
        'payee': { 'name': 'mock_name',  'email': 'mock_email' },
        'payment': { 'amount': 'mock_amount', 'currency': 'mock_currency' }
    }

    service.handle_event(mock_payload)

    requests.post.assert_called_once_with(
        "https://api.mailgun.net/v3/sandbox755e3e3d474a4b218e031f7213467c79.mailgun.org/messages",
        auth = ('api', '5ff5b93ffdea5568338776eaf366f060-8b7bf2f1-17f4b7c0'),
        data = {
            "from": "jessicalstenning@gmail.com",
            "to": "jessicalstenning@gmail.com",
            "subject": "Payment received",
            "text": ("""
                    Dear mock_name,

                    You have received a payment of mock_amount mock_currency from mock_name (mock_email).

                    Yours,

                    Student.com
                    """)})

def test_format_response_output():

    mock_data = {
        'client': { 'name': 'Wendy', 'email': 'wendy@email.com' },
        'payee': { 'name': 'Kris',  'email': 'kris@email.com' },
        'payment': { 'amount': '12345', 'currency': 'EUR' }
    }

    print(SendsMail().format_response_func(mock_data))

    assert SendsMail().format_response_func(mock_data) == {
        "from": "jessicalstenning@gmail.com",
        "to": "jessicalstenning@gmail.com",
        "subject": "Payment received",
            "text": ("""
                    Dear Kris,

                    You have received a payment of 12345 EUR from Wendy (wendy@email.com).

                    Yours,

                    Student.com
                    """)
    }
