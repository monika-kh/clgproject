from django.urls import path, include
from student_app import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("college/", views.CollegeView.as_view()),
    path("college/<int:pk>/", views.CollegeView.as_view(), name="college"),
    path("student/", views.StudentView.as_view()),
    path("student/<int:pk>/", views.StudentView.as_view(), name="student"),
    path('login_api/', obtain_auth_token, name='api_token_auth'),
    #path('rest-auth/', include('rest_auth.urls')),
]



