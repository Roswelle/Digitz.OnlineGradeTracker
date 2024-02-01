from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('teacherindex/', views.teacherindex, name="teacherindex"),
    path ('login/', views.login, name="login"),
    path ('register/', views.register, name="register"),
    path ('about/<int:teacher_pk>/', views.about, name="about"),
    path ('studentabout/<int:student_pk>/', views.studentabout, name="studentabout"),
    path ('studentgrades/<int:student_pk>/<int:course_pk>/', views.studentgrades, name="studentgrades"),
    path ('studentdashboard/<int:student_pk>/', views.studentdashboard, name="studentdashboard"),
    path ('teachergrading/<int:teacher_pk>/<int:course_pk>/', views.teachergrading, name="teachergrading"),
    path ('teacherdashboard/<int:teacher_pk>/', views.teacherdashboard, name="teacherdashboard"),
    path ('student/', views.studentindex, name="studentindex"),
    path ('studentprofile/<int:student_pk>/', views.studentprofile, name="studentprofile"),
    path ('teacherprofile/<int:teacher_pk>/', views.teacherprofile, name="teacherprofile"),
    path ('teacherform/<int:teacher_pk>/', views.teacherform, name="teacherform"),
    path ('gradeform/<int:teacher_pk>/<int:course_pk>/<int:student_pk>/', views.gradeform, name="gradeform"),
    path ('enrollform/<int:student_pk>/', views.enrollform, name="enrollform"),
    path ('addcourse/<int:teacher_pk>/', views.addcourse, name="addcourse"),
    path ('removecourse/<int:teacher_pk>/<int:course_pk>/', views.removecourse, name="removecourse"),
    path ('studentform/<int:student_pk>/', views.studentform, name="studentform"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
