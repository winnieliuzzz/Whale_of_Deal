import os

DEBUG = True
ADMINS = frozenset([
    os.environ.get('ADMIN_EMAIL')
])
GMAIL = os.environ.get('GMAIL')
PASSWORD = os.environ.get('GMAIL_PASSWORD')
DOMAIN = "https://whaleofdeal.herokuapp.com"