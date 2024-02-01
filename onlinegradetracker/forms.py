from django.forms import  ModelForm
from .models import *
from django import forms
from django.forms import DateInput
# login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateTeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class teacherUpdateForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['Teachername', 'Department', 'Birthday', 'ContactNumber', 'Email', 'gender']

class GradeEditForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['grade_value']

class EnrollForm(forms.Form):
    course_code = forms.CharField(max_length=50, label='Course Code')

class CourseAddForm(ModelForm):
    class Meta:
        model = Course
        fields = ['CourseName', 'CourseID', 'YearAndSection']
        
class TeacherProfileForm(ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['Picture']

class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['Picture']

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['FirstName', 'MiddleName', 'LastName', 'StudentID', 'YearAndSection', 'ContactNumber', 'Email']

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['FirstName', 'MiddleName', 'LastName', 'StudentID', 'YearAndSection', 'Status', 'Birthday', 'ContactNumber', 'Email']
        widgets = {
            'Birthday': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
class TeacherRegistrationForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['Teachername', 'Department', 'Birthday', 'ContactNumber', 'Email', 'gender']
        widgets = {
            'Birthday': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }