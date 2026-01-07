from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.name} - {self.subject}'


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=300, help_text="Comma separated list of technologies")
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="Skill level from 1 to 100")
    category = models.CharField(max_length=50, help_text="e.g., Frontend, Backend, Database, etc.")
    icon = models.CharField(max_length=50, blank=True, help_text="Optional CSS class for icon")
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    currently_working = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} at {self.company}'
