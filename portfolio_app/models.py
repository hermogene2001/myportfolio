from django.db import models
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(max_length=100, default="UKUNDAYEZU Hermogene")
    title = models.CharField(max_length=200, help_text="Your main title/role")
    bio = models.TextField(help_text="Brief bio that will be animated")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    headline_1 = models.CharField(max_length=200, help_text="First animated headline", default="Full Stack Developer")
    headline_2 = models.CharField(max_length=200, help_text="Second animated headline", default="Software Engineer")
    headline_3 = models.CharField(max_length=200, help_text="Third animated headline", default="Tech Enthusiast")
    
    # Contact Information
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    
    # Social Media Links
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


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


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, help_text="e.g., Bachelor of Science, Diploma, etc.")
    field_of_study = models.CharField(max_length=200, help_text="e.g., Computer Science, Information Technology")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text="Additional info about the program")
    grade = models.CharField(max_length=10, blank=True, null=True, help_text="GPA or grade")
    is_current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-end_date', '-start_date']
    
    def __str__(self):
        return f'{self.degree} in {self.field_of_study} from {self.school}'