from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from .models import Student, Parent, AcademicDetails, DocumentUpload
from .serializers import StudentSerializer, ParentSerializer, AcademicDetailsSerializer, DocumentUploadSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    parser_classes = [MultiPartParser]


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class AcademicDetailsViewSet(viewsets.ModelViewSet):
    queryset = AcademicDetails.objects.all()
    serializer_class = AcademicDetailsSerializer

class DocumentUploadViewSet(viewsets.ModelViewSet):
    queryset = DocumentUpload.objects.all()
    serializer_class = DocumentUploadSerializer
