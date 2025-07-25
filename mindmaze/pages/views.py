from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"MindMaze Feedback from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipient = ['your_email@gmail.com']  # your receiving email
            send_mail(subject, message, sender, recipient, fail_silently=False)
            messages.success(request, "Your message was sent successfully! 🙌")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})


def feedback_view(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        messages.success(request, "Thank you for your feedback!")
    return render(request, 'pages/feedback.html')

def features_view(request):
    return render(request, 'pages/features.html')

def blog_view(request):
    return render(request, 'pages/blog.html')


def privacy_policy_view(request):
    return render(request, 'pages/privacy_policy.html')

def terms_view(request):
    return render(request, 'pages/terms.html')

def cookie_policy_view(request):
    return render(request, 'pages/cookie_policy.html')


def faq_view(request):
    return render(request, 'pages/faq.html')
