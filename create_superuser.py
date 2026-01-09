import os
import django
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
import time
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

try:
    django.setup()
except Exception as e:
    print(f"Error setting up Django: {e}")
    sys.exit(1)

# Create superuser
try:
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created successfully!")
    else:
        print("Superuser 'admin' already exists.")
except Exception as e:
    print(f"Error creating superuser: {e}")
    # Retry after a delay in case of connection issues
    time.sleep(5)
    try:
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("Superuser 'admin' created successfully after retry!")
        else:
            print("Superuser 'admin' already exists after retry.")
    except Exception as e2:
        print(f"Failed to create superuser after retry: {e2}")
        sys.exit(1)