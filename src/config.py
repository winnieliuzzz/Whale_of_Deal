import os

DEBUG = True
ADMINS = frozenset([
    os.environ.get('ADMIN_EMAIL')
])
DOMAIN = "pricing.jslvtr.com"