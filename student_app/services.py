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
    def process(self):
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
        clg_obj = College.objects.get(id=data.get("student_data").get("college"))
        student_obj = Student.objects.create(
            college=clg_obj,
            first_name=student_data.get("first_name"),
            last_name=student_data.get("last_name"),
            branch=student_data.get("branch"),
            dob=student_data.get("dob"),
        )

        return student_obj


class GetRelatedStudentService(Service):
    def process(self):
        data = self.data
        pk = data.get("pk")

        related_name = Student.objects.filter(college_id=pk)  # get students related to a particular college id
        return related_name

    # query--> related_clg = Student.objects.filter(college_id=5)


class GetRegisterService(Service):
    def process(self):
        student_register = Student.objects.all()
        return student_register