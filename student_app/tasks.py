from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Student


@shared_task
def send_mail_to_all(email_msg, email_sub):
    students_in = Student.objects.all()

    for student in students_in:
        email = student.email
        send_mail(
            email_sub,
            email_msg,
            EMAIL_HOST_USER,
            [email],
            html_message=email_msg,
            fail_silently=False,
        )

