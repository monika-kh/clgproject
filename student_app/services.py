from .models import College, Student
from service_objects.services import Service


class CollegeService(Service):
    def process(self):
        clg_data = self.data
        data = clg_data.get("college_data")

        clg_obj = College.objects.create(
            college_name=data.get("college_name"),
            city=data.get("city"),
            state=data.get("state"),
        )
        return clg_data


class GetCollegeService(Service):
    def process(self):
        clg = self.data
        pk = clg.get('pk')
        if pk:
            college_gt = College.objects.get(id=pk)
        else:
            college_gt = College.objects.all()
        return college_gt
        # clg = College.objects.all()
        # return clg


class DeleteCollegeService(Service):
    def process(self):
        pk = self.data.get('pk')
        college_dlt = College.objects.get(pk=pk)
        college_dlt.delete()


class PutCollegeService(Service):
    def process(self):
        college_put = self.data  # data received from views
        clg = college_put.get('data')
        pk = clg.get('id')

        clg_put = College.objects.get(pk=pk)
        clg_name = clg.get('college_name')
        clg_city = clg.get('city')
        clg_state = clg.get('state')

        clg_put.college_name = clg_name
        clg_put.city = clg_city
        clg_put.state = clg_state
        clg_put.save()
        return clg_put


class GetStudentService(Service):
    def process(self):  # get data of particular id of student
        std = self.data
        pk = std.get("pk")
        if pk:
            student_gt = Student.objects.get(id=pk)
        else:
            student_gt = Student.objects.all()
        return student_gt

        # std = Student.objects.all()
        # return std


class CreateStudentService(Service):
    def process(self):
        data = self.data
        student_data = data.get("student_data")
        # get college object or college_id from college model or clg_service using student_data
        clg_obj = College.objects.get(college_name=data.get("student_data").get("college_name"))

        # student_obj = Student.objects.create(
        #     college=clg_obj,
        #     first_name=student_data.get("first_name"),
        #     last_name=student_data.get("last_name"),
        #     branch=student_data.get("branch"),
        #     dob=student_data.get("dob"),
        # )                                                              #obj created when abstractuser is not used
        student_obj = Student.objects.create(
            college=clg_obj,
            first_name=student_data.get('college_student')[0].get('first_name'),
            last_name=student_data.get('college_student')[0].get("last_name"),
            branch=student_data.get('college_student')[0].get("branch"),
            dob=student_data.get('college_student')[0].get("dob"),
            username=student_data.get('college_student')[0].get("username"),
            email=student_data.get('college_student')[0].get("email"),
            address=student_data.get('college_student')[0].get("address"),
            #password=student_data.get('college_student')[0].get("password"),
            #college=student_data.get('college_student')[0].get("college")
        )
        student_obj.set_password("password")
        student_obj.save()
        return student_obj


class GetRelatedStudentService(Service):
    def process(self):
        data = self.data
        pk = data.get("pk")
        related_name = Student.objects.filter(college_id=pk)  # get students related to a particular college id
        return related_name

    # query--> related_clg = Student.objects.filter(college_id=5)


class DeleteRelatedStudentService(Service):
    def process(self):
        dlt_data = self.data
        pk = dlt_data.get('pk')
        std_dlt = Student.objects.get(pk=pk)
        std_dlt.delete()


































































# class GetRegisterService(Service):
#     def process(self):
#         student_register = Student.objects.all()
#         return student_register
#
#
# class CreateRegisterService(Service):
#     def process(self):
#         college_student_data = self.data
#         clg_std = college_student_data.get("register_data")
#         college_data = clg_std.get('college')
#         breakpoint()
