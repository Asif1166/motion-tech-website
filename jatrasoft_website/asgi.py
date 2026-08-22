"""
ASGI config for jatrasoft_website project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jatrasoft_website.settings')

application = get_asgi_application()

