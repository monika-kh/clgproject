from django.db import models

# Create your models here.


class College(models.Model):
    college_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    class Meta:
        db_table = 'College'


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='college_student')
    dob = models.DateField()

    class Meta:
        db_table = 'Student'

