from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Experience, Contact


def home(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Validate form data
        if name and email and subject and message:
            # Create and save contact form entry
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            
            # Send email notification
            try:
                send_mail(
                    subject=f'Portfolio Contact: {subject}',
                    message=f'From: {name}\nEmail: {email}\n\nMessage:\n{message}',
                    from_email=email,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                # Still save the contact even if email fails
                messages.warning(request, 'Your message has been saved but there was an issue sending the email notification.')
        else:
            messages.error(request, 'Please fill in all required fields.')
        
        return redirect('home')
    
    # For GET requests, render the home page with data
    projects = Project.objects.all().order_by('-date_created')
    # Process technologies for each project
    for project in projects:
        project.technologies_list = [tech.strip() for tech in project.technologies.split(',')]
    
    context = {
        'projects': projects,
        'skills': Skill.objects.all().order_by('category'),
        'experiences': Experience.objects.all().order_by('-start_date'),
    }
    return render(request, 'portfolio/index.html', context)
