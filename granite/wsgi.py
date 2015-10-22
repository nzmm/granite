"""
WSGI config for granite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

workspace = os.path.dirname(os.path.dirname(__file__))
if workspace not in sys.path:
    sys.path.append(workspace)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "granite.settings")

application = get_wsgi_application()
