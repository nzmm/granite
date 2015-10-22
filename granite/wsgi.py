"""
WSGI config for granite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.chdir('/home/matthew/granite')


print('granite.wsgi', os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "granite.settings")

application = get_wsgi_application()
