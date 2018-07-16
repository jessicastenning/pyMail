# PyMail

PyMail is a nameko service that sends an email via Mailgun whenever an event is received from another service. PyMail mimics a payment receipt email service using dummy user information supplied via Faker.

### Installation

From the command line, clone this repository to your machine.
```
git clone https://github.com/jessicastenning/pyMail.git
```
You will then need to install the following (if they are not already installed)

Nameko:
```
pip install nameko
```
Pytest:
```
pip install -U pytest
```
Faker:
```
pip install fake-factory
```
Mailgun:

PyMail uses mailgun to send emails. In order to get this service running locally, you will need to sign up for a mailgun account via the website

https://www.mailgun.com/

You will then need to update the information in the constants file (API key, email, and domain) for your own Mailgun account information. All of these can be found on your main mailgun dashboard.

The your domain will be in the following format:
```
https://api.mailgun.net/v3/<insert your domain here>.mailgun.org/messages
```

### Running the program

Open two new terminal shells.

In the first shell write the following command:
```
nameko run sends_mail
```

In the second window write the following command:
```
nameko run payments
```

As long as both services are running, pyMail will continue to send out payment confirmation emails for each event, including the information supplied by Faker.

Every time an event occurs, the sends_mail terminal will print the information received from payments, and send an email via mailgun - similar to the following: 
```
Connected to amqp://guest:**@127.0.0.1:5672//
('payment received:', {u'payee': {u'name': u'Deborah Bennett', u'email': u'tmcgee@example.com'},
u'client': {u'name': u'Brett Garcia', u'email': u'juarezyolanda@example.com'}, u'payment': 
{u'currency': u'EUR', u'amount': 5188}})
```
Example email:
```
Dear Deborah Bennett,

You have received a payment of 5188 EUR from Brett Garcia (juarezyolanda@example.org).

Yours,

Student.com
```
### Testing 

Pytest was used for testing. 

To run pytest from your terminal write the following command: 
```
pytest test_sends_mail.py
```
### Areas for continued improvement
Due to my unfamiliarity with Python/Namkeo/Pytest, I found the testing aspect of this test the most challenging/time consuming - had I had more time to complete my program I'd have liked to have continued to implement more rigorous tests, and include error messages etc. 

Given the time frame, I decided to focus on successfully mocking/testing my handle event function, as I felt this was the most challenging and therefore best demonstrated technical ability. 
