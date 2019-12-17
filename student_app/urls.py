from django.urls import path
from student_app import views

urlpatterns = [
    path('college/', views.CollegeView.as_view()),
    path('college/<int:pk>/', views.CollegeView.as_view(), name='college'),
    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentView.as_view(), name='student')
]