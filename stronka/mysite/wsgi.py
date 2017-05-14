from django.core.wsgi import get_wsgi_application

"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

sys.path.insert(0, "/var/www")
sys.path.insert(0, "/var/www/monitoring")
sys.path.insert(0, "/var/www/monitoring/stronka")
sys.path.insert(0, "/var/www/monitoring/stronka/mysite")
sys.path.append('/usr/local/lib/python3.6/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
