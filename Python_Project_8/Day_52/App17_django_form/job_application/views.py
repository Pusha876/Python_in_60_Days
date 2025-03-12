from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            Last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                Last_name=Last_name,
                email=email,
                date=date,
                occupation=occupation
            )

            message_body = (
                f"A new job application was submitted by {first_name} "
                f"{Last_name} on {date} for the position of {occupation}."
            )
            email_message = EmailMessage(
                "Form submission confirmation", message_body, to=[email]
            )
            email_message.send()

            messages.success(request, "Form submitted successfully!")
        else:
            messages.error(
                request,
                'Form submission failed. Please correct the errors and try '
                'again.'
            )

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
