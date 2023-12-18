# models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    adhar_card_number = models.CharField(max_length=12)
    dob = models.DateField()
    identification_marks = models.TextField()
    admission_category = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    mail_id = models.EmailField()
    contact_detail = models.CharField(max_length=15)
    address = models.TextField()

class Parent(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='parent')
    father_name = models.CharField(max_length=255)
    father_qualification = models.CharField(max_length=255)
    father_profession = models.CharField(max_length=255)
    father_designation = models.CharField(max_length=255)
    father_aadhar_card = models.CharField(max_length=12)
    father_mobile_number = models.CharField(max_length=15)
    father_mail_id = models.EmailField()

    mother_name = models.CharField(max_length=255)
    mother_qualification = models.CharField(max_length=255)
    mother_profession = models.CharField(max_length=255)
    mother_designation = models.CharField(max_length=255)
    mother_aadhar_card = models.CharField(max_length=12)
    mother_mobile_number = models.CharField(max_length=15)
    mother_mail_id = models.EmailField()

class AcademicDetails(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='academic_details')
    enrollment_id = models.CharField(max_length=255)
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    doj = models.DateField()

class DocumentUpload(models.Model):
    ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx']

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='document_uploads')
    document = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)]
    )
