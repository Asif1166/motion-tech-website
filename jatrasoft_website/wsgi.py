"""
WSGI config for jatrasoft_website project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jatrasoft_website.settings')

application = get_wsgi_application()

