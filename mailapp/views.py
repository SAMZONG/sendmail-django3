from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method=='POST':
        emailID = request.POST.get('emailID')
        name = request.POST.get('name')
        message = request.POST.get('message')

        subject = 'Contact Form | {}'.format(name)
        my_email = ['jerinthomas17@gmail.com']
        body = "Name : {0}\n\nEmail ID : {1}\n\nMessage : {2}".format(name, emailID, message)

      # send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
        send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        my_email,
        fail_silently = False
        )
    return render(request, 'mailapp/index.html')
