"""
WSGI config for shmoothies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import pymysql
pymysql.install_as_MySQLdb()

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/claremont-newsletter/backend')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
