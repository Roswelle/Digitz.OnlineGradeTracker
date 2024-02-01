from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
import random
import string



class Student(models.Model):
    FirstName = models.CharField(max_length=50, null=True)
    MiddleName = models.CharField(max_length=50, null=True)
    LastName = models.CharField(max_length=50, null=True)
    StudentID = models.IntegerField(blank=True)
    YearAndSection = models.CharField(max_length=50, null=True)
    Status = models.CharField(max_length=50, choices=[('regular','Regular'),('irregular','Irregular')], null=False)
    Birthday = models.DateField(max_length=50, blank=True)
    ContactNumber = models.IntegerField(blank=True)
    Email = models.EmailField(max_length=50, blank=True)
    
    def __str__ (self):
        return f"{self.FirstName} {self.LastName}"
    
    def get_enrolled_courses(self):
        return self.courses_enrolled.all()



class Course(models.Model):
    CourseName = models.CharField(max_length=50, null=True)
    CourseID = models.CharField(max_length=50, null=True)
    CourseCode = models.CharField(max_length=50, unique=True, null=True)
    YearAndSection = models.CharField(max_length=50, null=True)
    students_enrolled = models.ManyToManyField(Student, related_name='courses_enrolled', blank=True)

    def __str__(self):
        return f"{self.CourseID} - {self.YearAndSection}"

    def save(self, *args, **kwargs):
        if not self.CourseCode:
            self.CourseCode = self.generate_unique_course_code()
        super().save(*args, **kwargs)

    def generate_unique_course_code(self):
        length = 5
        characters = string.ascii_uppercase + string.digits
        while True:
            course_code = ''.join(random.choice(characters) for _ in range(length))
            if not Course.objects.filter(CourseCode=course_code).exists():
                return course_code

    
class Teacher(models.Model):
    Teachername = models.CharField(max_length=50, null=True)
    Department = models.CharField(max_length=50, null=True)
    Birthday = models.DateField(max_length=50, blank=True)
    ContactNumber = models.IntegerField(blank=True)
    Email = models.EmailField(max_length=50, blank=True)
    course_taught = models.ManyToManyField(Course, related_name='teachers_courses')
    gender = models.CharField(max_length=10, choices=[('male','Male'), ('female','Female'), ('other','Other')], default="Other")

    def __str__ (self):
     return self.Teachername
    
    def get_current_courses(self):
        return self.course_taught.all()


class TeacherProfile(models.Model):
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, related_name='teacherprofile')
    Picture = models.ImageField(upload_to='images/', default='images/default.png') 

    def __str__ (self):
        return f"{self.user}'s Profile"
    
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    Picture = models.ImageField(upload_to='images/', default='images/default.png')

    def __str__ (self):
        return f"{self.student}'s Profile"
    
    
class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    grade_value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    grade_date = models.DateField(default=timezone.now)

    def __str__ (self):
       return f"{self.student.FirstName} {self.student.LastName}'s Grade in {self.course.CourseName}"

