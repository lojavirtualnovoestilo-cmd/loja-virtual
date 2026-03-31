"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
import django
from django.core.management import call_command
from django.contrib.auth.models import User

# Rodar migrações e criar usuário automaticamente ao iniciar
try:
    django.setup()
    call_command('migrate', interactive=False)
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@email.com', 'admin123')
except Exception as e:
    print(f"Erro ao iniciar banco: {e}")
