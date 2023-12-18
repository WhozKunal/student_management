# yourappname/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ParentViewSet, AcademicDetailsViewSet, DocumentUploadViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'academic-details', AcademicDetailsViewSet)
router.register(r'document-upload', DocumentUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
