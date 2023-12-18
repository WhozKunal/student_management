
from django.apps import AppConfig

class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'

    def ready(self):
        import student.signals  # Add this line to connect signals when the app is ready
