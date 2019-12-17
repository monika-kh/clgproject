from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import College, Student
from .serializers import CollegeSerializer, Student1Serializer, RelatedCollegeSerializer, StudentSerializer
from .services import (CollegeService, GetCollegeService, DeleteCollegeService, PutCollegeService,
                       GetStudentService, CreateStudentService, GetRelatedStudentService, GetStudentService)
#Create your views here.


class CollegeView(APIView):
    def post(self, request):
        college_data = request.data
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            college = CollegeService.execute({'college_data': request.data})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, pk=None):                                          # pk is used to get clg id
        college_gt = GetCollegeService.execute({'pk': pk})
        if pk:
            serializer = CollegeSerializer(college_gt)
        else:
            serializer = CollegeSerializer(college_gt, many=True)
        return Response(serializer.data)

    # clg_get = GetCollegeService.execute({})
        # serializer = CollegeSerializer(clg_get, many=True)
        # return Response(serializer.data)

    def delete(self, request, pk):
        DeleteCollegeService.execute({'pk': pk})
        return Response(data={'Message': 'deleted'}, status=200)

    def put(self, request, pk):
        college_put = College.objects.get(pk=pk)
        data = request.data
        serializer = CollegeSerializer(college_put, data=request.data)
        if serializer.is_valid():
            # PutCollegeService.execute({'pk': pk})
            PutCollegeService.execute({'college_put': college_put, 'data': request.data})  # data sent to services
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):
    def get(self, request, pk=None):
        student_get = GetStudentService.execute({'pk': pk})                # data using primary key
        if pk:
            serializer = Student1Serializer(student_get)
        else:
            serializer = Student1Serializer(student_get, many=True)
        return Response(serializer.data)

        # student_get = GetStudentService.execute({})                     # get all data
        # serializer = StudentSerializer(student_get, many=True)
        # return Response(serializer.data)

    def post(self, request):
        student_data = request.data
        serializer = Student1Serializer(data=student_data)                  # when obj is not created
        if serializer.is_valid(raise_exception=True):
            college = CreateStudentService.execute({'student_data': request.data})
            ser1 = Student1Serializer(college)                               # when obj is created
            return Response(ser1.data, status=201)
        return Response(serializer.errors, status=400)

    def get (self, request, pk=None):              # get students related to a particular college id
        related_student = GetRelatedStudentService.execute({'pk': pk})
        college_gt = GetCollegeService.execute({'pk': pk})
        if pk:
            serializer = RelatedCollegeSerializer(college_gt)
        else:
            serializer = RelatedCollegeSerializer(college_gt, many=True)
        return Response(serializer.data)











