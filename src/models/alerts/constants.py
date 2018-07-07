import os

ALERT_TIMEOUT = 1
COLLECTION = "alerts"
URL = os.environ.get('MAILGUN_URL') #"https://api.mailgun.net/v3/sandboxe93419791fcd479e915febdac8e6de33.mailgun.org/messages"
API_KEY = os.environ.get('MAILGUN_API_KEY') #"0243d99130a4f019a9351e125a52693e-47317c98-1203736f"
FROM = os.environ.get('MAILGUN_FROM') #"WhaleofDeal postmaster@sandboxe93419791fcd479e915febdac8e6de33.mailgun.org"