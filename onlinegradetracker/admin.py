from django.contrib import admin
from .models import Student,Teacher,Grade,Course,TeacherProfile,StudentProfile


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
