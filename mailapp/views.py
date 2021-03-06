from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def home (request):
    if request.method == 'POST':
        emailID = request.POST.get('emailID')
        name = request.POST.get('name')
        message = request.POST.get('message')
        html_message = "<h4>Thank you for checking us out, your message has been well received.</h4><br>If it's a remark/feedback, we Thank you in advance : ) <br>If its a suggestion ? I pinky swear, I'll work on it : ))<br><br><i>Thank you,<i><br><i>Jerin Thomas<i><br>"
        
        subject = 'Contact Form | {}'.format(name)
        # my_email = ['samzong.lu@gmail.com']
        body = "Name : {0}\n\nEmail ID : {1}\n\nMessage : {2}".format(name, emailID, message)
        body2 = "This is a test message"
        
        # send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
        send_mail(subject=subject, message=body, from_email=settings.EMAIL_HOST_USER, recipient_list=[emailID, ],
                  fail_silently=False)
        send_mail(subject="Thank you for reaching out to us", message=body2, from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[emailID, ], fail_silently=False, html_message=html_message)
    
    return render(request, 'mailapp/index.html')
