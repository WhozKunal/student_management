# serializers.py
from rest_framework import serializers
from .models import Student, Parent, AcademicDetails, DocumentUpload

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class AcademicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDetails
        fields = '__all__'

class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentUpload
        fields = '__all__'

# serializers.py

class StudentSerializer(serializers.ModelSerializer):
    parent = ParentSerializer()
    academic_details = AcademicDetailsSerializer()
    document_uploads = DocumentUploadSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        parent_data = validated_data.pop('parent')
        academic_details_data = validated_data.pop('academic_details')
        document_uploads_data = validated_data.pop('document_uploads', [])

        student = Student.objects.create(**validated_data)

        Parent.objects.create(student=student, **parent_data)
        AcademicDetails.objects.create(student=student, **academic_details_data)

        for document_upload_data in document_uploads_data:
            DocumentUpload.objects.create(student=student, **document_upload_data)

        return student

    def update(self, instance, validated_data):
        parent_data = validated_data.pop('parent')
        academic_details_data = validated_data.pop('academic_details')
        document_uploads_data = validated_data.pop('document_uploads', [])

        instance.name = validated_data.get('name', instance.name)
        # Update other fields as needed

        instance.parent.father_name = parent_data.get('father_name', instance.parent.father_name)
        # Update other parent fields as needed

        instance.academic_details.enrollment_id = academic_details_data.get('enrollment_id', instance.academic_details.enrollment_id)
        # Update other academic details fields as needed

        # Update document uploads if needed

        instance.save()
        instance.parent.save()
        instance.academic_details.save()

        return instance

    def delete(self, instance):
        instance.delete()
        return instance
