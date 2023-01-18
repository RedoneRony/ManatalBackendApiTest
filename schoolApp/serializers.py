from django.db.models import fields
from rest_framework import serializers
from .models import (
    School,
    Student,
)


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [ "id","firstName","lastName","nationality","age","studentIdentificationNumber", "schoolName"]

    def create(self, validated_data):
        school_id = self.context["schoolName_id"]
        school = School.objects.get(id=school_id)
        serializer = SchoolSerializer(school, many=False)
        if serializer.data["maximum_number_of_students"] > 0:
            school.maximum_number_of_students = serializer.data["maximum_number_of_students"] - 1
            school.save()
            return Student.objects.create(schoolName_id = school_id,  **validated_data)
        else:
            raise serializers.ValidationError("This School didn't had space to add new student")
        


class SchoolSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = "__all__"