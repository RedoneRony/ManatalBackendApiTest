from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from schoolApp.models import School, Student
# import Serializer's model
from schoolApp.serializers import StudentSerializer, SchoolSerializer



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
def getSchoolsInfo(request):
    school = School.objects.all()
    serializer = SchoolSerializer(school, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSchoolById(request, pk):
    school = School.objects.get(_id=pk)
    serializer = SchoolSerializer(school, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateSchoolInfo(request, pk):
    data = request.data
    school = School.objects.get(_id=pk)
    school.name = data['name']
    school.location = data['location']
    school.maximum_number_of_students = data['maximum_number_of_students']
    school.save()
    serializer = SchoolSerializer(school, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteSchool(request, pk):
    school = School.objects.get(_id=pk)
    school.delete()
    return Response('School deleted')



@api_view(['POST'])
def createStudent(request):
    data = request.data
    name = data["schoolName"]
    school = School.objects.get(name=name)
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
            return Response("School Name Not Exist or didn't had space to add new student")



@api_view(['GET'])
def getStudentInfo(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudentById(request, pk):
    student = Student.objects.get(_id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateStudentInfo(request, pk):
    data = request.data
    student = Student.objects.get(_id=pk)
    student.firstName = data['firstName']
    student.lastName = data['lastName']
    student.nationality = data['nationality']
    student.age = data['age']
    student.save()
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(_id=pk)
    serializer = StudentSerializer(student, many=False)
    if serializer.data !=[]:
        school = School.objects.get(name=serializer.data['schoolName'])
        serializer2 = SchoolSerializer(school, many=False)
        school.maximum_number_of_students = serializer2.data["maximum_number_of_students"] + 1
        school.save()
        student.delete()
        return Response('Student deleted')