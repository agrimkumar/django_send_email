from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render


from .core.email import send_mail
# Create your views here.

def send_email(request):

    email = "agrimtesting@gmail.com"

    context = {
        "user": request.user,
        "username": request.user.username
    }

    send_mail(
        to=email,
        subject_template="MailApp/mail_sub.txt",
        body_template="MailApp/mail.html",
        context=context
    )

    return HttpResponse("<h1> Sent Email</h1>")