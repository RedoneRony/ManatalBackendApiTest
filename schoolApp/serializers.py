from django.db.models import fields
from rest_framework import serializers
from .models import (
    School,
    Student,
)


class StudentSerializer(serializers.ModelSerializer):
    schoolName = serializers.CharField(source="schoolName.name", read_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = "__all__"