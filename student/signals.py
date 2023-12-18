# app/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Student

@receiver(post_save, sender=Student)
def send_email_on_student_creation(sender, instance, created, **kwargs):
    if created:
        subject = 'New Student Registration'
        message = f'The student {instance.name} has been registered.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['durganand.jha@habrie.com']  # Add your recipient email(s) here
        send_mail(subject, message, from_email, recipient_list)
