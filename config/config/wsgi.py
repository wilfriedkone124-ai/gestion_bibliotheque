"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import os
import sys

# Ajoutez le chemin absolu vers le dossier racine de votre projet
path = '/home/wilfrieddoh/gestion_bibliotheque'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

# Définissez le module de paramètres de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
