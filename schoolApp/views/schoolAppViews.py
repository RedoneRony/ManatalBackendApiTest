from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from schoolApp.models import School, Student
# import Serializer's model
from schoolApp.serializers import StudentSerializer, SchoolSerializer
# Create your views here.
def home(request):
    return HttpResponse("Hello World")


@api_view(['POST'])
def createSchool(request):
    data = request.data
    school = School.objects.create(
        name=data['name'],
        location=data['location'],
        maximum_number_of_students=data['maximum_number_of_students'],
    )
    school.save()
    schoolSerializer = SchoolSerializer(school)
    return Response(schoolSerializer.data)


@api_view(['GET'])
def getSchools(request):
    school = School.objects.all()
    serializer = SchoolSerializer(school, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def updateCategory(request, pk):
    data = request.data
    school = School.objects.get(_id=pk)
    school.name = data['name']
    school.location = data['location']
    school.maximum_number_of_students = data['maximum_number_of_students']
    school.save()
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCategory(request, pk):
    school = School.objects.get(_id=pk)
    school.delete()
    return Response('School deleted')