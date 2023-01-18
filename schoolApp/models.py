from django.db import models
import uuid
from django.db.models.deletion import CASCADE
# Create your models here.

# school model
class School(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=20, blank = False, null = False)
    location = models.CharField(max_length=30, null=True, blank=True)
    maximum_number_of_students = models.IntegerField(blank = False, null = False)

    def __str__(self):
        return self.name


# student model
class Student(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    schoolName = models.ForeignKey(School, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50, blank = False, null = False)
    lastName = models.CharField(max_length=50, blank = False, null = False)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    studentIdentificationNumber = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.firstName