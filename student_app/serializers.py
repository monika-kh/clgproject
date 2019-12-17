from .models import College, Student
from rest_framework import serializers


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class College1Serializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['college_name', 'city']


class Student1Serializer(serializers.ModelSerializer):  # fields='__all'--serializer used when only clg_id is needed
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'branch')


class RelatedCollegeSerializer(serializers.ModelSerializer):
    college_student = Student1Serializer(many=True)

# college serializer inherited with student1serializer and have related name 'college_student'
    class Meta:
        model = College
        fields = ('college_name', 'city', 'college_student')


class StudentSerializer(serializers.ModelSerializer):        # used when we want show particular fields of college model
    college = CollegeSerializer()
    class Meta:
        model = Student
        fields = '__all__'


# class RelatedStudentSerializer(serializers.ModelSerializer):  # serializer used when only clg_id is needed
#     class Meta:
#         model = Student
#         fields = '__all__'
