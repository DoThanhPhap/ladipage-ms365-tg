"""
Passenger WSGI entry point for DirectAdmin Python hosting.
"""
import os
import sys

# Add the project directory to the path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django
import django
django.setup()

# Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
