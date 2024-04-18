"""
WSGI config for will_be_there project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

# Load environment variables from .env file
dotenv.load_dotenv()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'will_be_there.settings')

application = get_wsgi_application()

