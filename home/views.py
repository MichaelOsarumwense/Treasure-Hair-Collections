from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from .forms import ContactForm
from django.contrib import auth, messages


def index(request):
    """ A View to return the index page """

    return render(request, 'home/index.html')


def view_about(request):
    """A View that renders the about page"""
    return render(request, "home/about.html")


def view_faqs(request):
    """A View that renders the FAQs page"""
    return render(request, "home/faqs.html")


def view_contact(request):
    """View handle contact form requests"""
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            message = request.POST['message']
            subject = request.POST['subject']
            send_mail(
                subject,
                "Message from: " +
                request.POST['email'] +
                "Message: " +
                message,
                'from@example.com',
                ['michael.oosarumwense@gmail.com'],
                fail_silently=False,
            )
            messages.success(request,
                             "Your message has been sent successfully!",
                             extra_tags="alert-success")
            return redirect(reverse('home'))
        else:
            messages.error(request, "Unable to send message at this time",
                                    extra_tags="alert-danger")
    else:
        contact_form = ContactForm()
    return render(request, 'home/contact.html', {'contact_form': contact_form})
