from rest_framework import serializers

from .models import College, Student


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = "__all__"


class College1Serializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ["college_name", "city"]


class Student1Serializer(serializers.ModelSerializer):  # fields='__all'--serializer used when only clg_id is needed
    class Meta:
        model = Student
        # fields = ("first_name", "last_name", "branch", "password", "password1", "username")
        fields = '__all__'
        extra_kwargs = {
            'branch': {'default': 'branch'},
            'password': {'default': 'password'},
            'username': {'default': 'username'},
            'password1': {'default': 'password1'}
        }                                                                 # to remove field required error.


class RelatedCollegeSerializer(serializers.ModelSerializer):
    college_student = Student1Serializer(
        many=True)  # college serializer inherited with student1serializer and have related name 'college_student'

    class Meta:
        model = College
        fields = ("id", "college_name", "city", "college_student")


class StudentSerializer(serializers.ModelSerializer):  # used when we want show particular fields of college model
    college = CollegeSerializer()

    class Meta:
        model = Student
        fields = "__all__"




















# class LoginInSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('username', 'password')
#
# class AuthUserSerializer(serializers.ModelSerializer):
#     auth_token = serializers.SerializerMethodField()
#
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
#         read_only_fields = ('id', 'is_active', 'is_staff')
#
#         User = get_user_model()
#
#         class UserLoginSerializer(serializers.Serializer):
#             email = serializers.CharField(max_length=300, required=True)
#             password = serializers.CharField(required=True, write_only=True
#
#
#
#             def get_auth_token(self, obj):
#                 token = Token.objects.create(user=obj)
#                 return token.key
#



















# class RelatedStudentSerializer(serializers.ModelSerializer):  # serializer used when only clg_id is needed
#     college_student = CollegeSerializer(many=True)
#
#     class Meta:
#         model = Student
#         fields = ("first_name", "last_name", "branch")
#

# class StudentRegisterSerializer(serializers.ModelSerializer):
#     # fields='__all'--serializer used when only clg_id is needed
#     college = RelatedCollegeSerializer()
#
#     class Meta:
#         model = Student
#         fields = '__all__'
