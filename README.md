# UKUNDAYEZU Hermogene - Portfolio Website

This is a Django-based single-page portfolio website featuring modern design and responsive layout.

## Features

- **Single-page layout** with smooth navigation between sections
- **Home/Hero section** - Professional introduction
- **About Me section** - Personal information and bio
- **Skills/Technologies section** - Visual representation of skills with progress bars
- **Projects/Portfolio section** - Interactive project showcase with images and links
- **Experience section** - Timeline of professional experience
- **Contact Form** - With database storage and email notifications
- **Responsive Design** - Works perfectly on desktop and mobile devices
- **Django Admin Panel** - For easy content management

## Technologies Used

- Django 5.0.7
- Python 3
- HTML5 & CSS3
- Bootstrap 5
- Font Awesome Icons
- jQuery
- SQLite Database

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies (if any additional packages needed):
   ```
   pip install -r requirements.txt
   ```
   Or install Django if not already installed:
   ```
   pip install django
   ```
4. Run database migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Configuration

1. Update email settings in `portfolio/settings.py`:
   - Set `EMAIL_HOST_USER` to your email address
   - Set `EMAIL_HOST_PASSWORD` to your app password
   - Adjust `EMAIL_HOST` and `EMAIL_PORT` if using a different provider

2. Customize content in the Django admin panel at `/admin/`

## Structure

- `portfolio/` - Main Django project settings
- `portfolio_app/` - Main application with views and models
- `templates/portfolio/` - HTML templates for the portfolio
- `static/css/` - Custom CSS styles
- `media/` - Uploaded files (projects images)
- `manage.py` - Django management commands

## Admin Access

- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Add/update projects, skills, experience, and contact entries
- Manage submitted contact form messages

## Customization

- Edit content through the Django admin panel
- Modify styles in `static/css/style.css`
- Update the template in `templates/portfolio/index.html`
- Add/remove sections as needed

## Deployment

For production deployment:
1. Update `DEBUG = False` in settings
2. Set proper `ALLOWED_HOSTS` environment variable (on Render: set environment variable `ALLOWED_HOSTS` to your domain like `your-app-name.onrender.com`)
3. Configure a production-ready database
4. Install Gunicorn: `pip install gunicorn`
5. Collect static files: `python manage.py collectstatic --noinput`
6. Run with Gunicorn: `gunicorn portfolio.wsgi:application`

## Contact Form

The contact form stores submissions in the database and optionally sends email notifications. Submissions can be viewed in the Django admin panel.

---

Built with ❤️ using Django.