from django.shortcuts import render
from rest_framework.response import Response
from schoolApp.models import School, Student
from rest_framework import filters
from schoolApp.serializers import StudentSerializer, SchoolSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend 

class SchoolsViewSet(ModelViewSet):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['id', 'name']

    def create(self, request, *args, **kwargs):
        data = request.data
        school = School.objects.create(
            name=data['name'],
            location=data['location'],
            maximum_number_of_students=data['maximum_number_of_students'],
        )
        school.save()
        schoolSerializer = SchoolSerializer(school)
        return Response(schoolSerializer.data)

    def put(self, request, *args, **kwargs):
        data = request.data
        school = School.objects.get()
        school.name = data['name']
        school.location = data['location']
        school.maximum_number_of_students = data['maximum_number_of_students']
        school.save()
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        school = self.get_object()
        school.delete()
        return Response('School deleted')


class SchoolsStudentsViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
         return Student.objects.filter(schoolName_id=self.kwargs["school_pk"])
    
    def get_serializer_context(self):
        return {"schoolName_id": self.kwargs["school_pk"]}


class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'age']
    search_fields = ['id', 'age']
    

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data["schoolName"]

        try:
            school = School.objects.get(id=name)
            serializer = SchoolSerializer(school, many=False)
            if serializer.data !=[]:
                if serializer.data["maximum_number_of_students"] > 0:
                    school.maximum_number_of_students = serializer.data["maximum_number_of_students"] - 1
                    school.save()
                    student = Student.objects.create(
                        schoolName=school,
                        firstName=data['firstName'],
                        lastName=data['lastName'],
                        nationality=data['nationality'],
                        age=data['age']
                    )
                    student.save()
                    studentSerializer = StudentSerializer(student)
                    return Response(studentSerializer.data)
                else:
                    return Response("This School didn't had space to add new student") 

        except ObjectDoesNotExist:
            return Response("This School is not exist")


    def put(self, request, *args, **kwargs):
        data = request.data
        student = Student.objects.get(id=pk)
        student.firstName = data['firstName']
        student.lastName = data['lastName']
        student.nationality = data['nationality']
        student.age = data['age']
        student.save()
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = StudentSerializer(student, many=False)

        if serializer.data !=[]:
            school = School.objects.get(id=serializer.data['schoolName'])
            serializer2 = SchoolSerializer(school, many=False)
            school.maximum_number_of_students = serializer2.data["maximum_number_of_students"] + 1
            school.save()
            student.delete()
            return Response('Student deleted')