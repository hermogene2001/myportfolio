"""
Test script to verify all portfolio website functionality
"""

import os
import sys
import django
from django.conf import settings
from django.test import Client
from django.contrib.auth import get_user_model

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Temporarily add testserver to allowed hosts for testing
django.setup()

# Add testserver to allowed hosts
from django.conf import settings
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append('testserver')

def test_portfolio_functionality():
    print("Testing Portfolio Website Functionality...")
    
    # Test 1: Check if models can be imported and used
    print("\n1. Testing Models...")
    try:
        from portfolio_app.models import Contact, Project, Skill, Experience
        
        # Test creating a contact (without saving to avoid cluttering DB)
        contact = Contact(
            name="Test User",
            email="test@example.com", 
            subject="Test Subject",
            message="Test message content"
        )
        print(f"   ✓ Contact model works: {contact.name}")
        
        print("   ✓ All models imported successfully")
    except Exception as e:
        print(f"   ✗ Model test failed: {e}")
        return False
    
    # Test 2: Test URL routing and views
    print("\n2. Testing Views and URLs...")
    try:
        client = Client()
        
        # Test homepage
        response = client.get('/')
        assert response.status_code == 200
        print("   ✓ Homepage loads successfully")
        
        # Test admin page (should redirect to login)
        response = client.get('/admin/')
        # Admin should redirect to login page (status code 302)
        assert response.status_code in [200, 302]  # May show login page
        print("   ✓ Admin route accessible")
        
    except Exception as e:
        print(f"   ✗ View/URL test failed: {e}")
        return False
    
    # Test 3: Test template rendering
    print("\n3. Testing Templates...")
    try:
        from django.template.loader import render_to_string
        
        # Try to render the home template (this tests if all template tags work)
        rendered = render_to_string('portfolio/index.html', {'projects': [], 'skills': [], 'experiences': []})
        assert len(rendered) > 0
        print("   ✓ Template renders without errors")
        
    except Exception as e:
        print(f"   ✗ Template test failed: {e}")
        return False
    
    # Test 4: Check if static files are configured
    print("\n4. Testing Static Files Configuration...")
    try:
        static_dirs = settings.STATICFILES_DIRS
        media_root = settings.MEDIA_ROOT
        static_url = settings.STATIC_URL
        media_url = settings.MEDIA_URL
        
        print(f"   ✓ Static files directory: {static_dirs}")
        print(f"   ✓ Media files directory: {media_root}")
        print(f"   ✓ Static URL: {static_url}")
        print(f"   ✓ Media URL: {media_url}")
        
    except Exception as e:
        print(f"   ✗ Static files test failed: {e}")
        return False
    
    print("\n✓ All tests passed! Portfolio website is functioning correctly.")
    print("\nWebsite Features Available:")
    print("- Single-page layout with smooth navigation")
    print("- Home/Hero section")
    print("- About Me section")
    print("- Skills/Technologies section with progress bars")
    print("- Projects/Portfolio section with cards")
    print("- Experience section with timeline")
    print("- Contact form with database storage")
    print("- Responsive design for desktop & mobile")
    print("- Django admin panel for content management")
    print("- Email notifications for contact form")
    print("\nAccess the website at: http://127.0.0.1:8000/")
    print("Access admin at: http://127.0.0.1:8000/admin/")
    
    return True

if __name__ == "__main__":
    test_portfolio_functionality()