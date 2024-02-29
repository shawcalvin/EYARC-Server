from django.urls import path
from .assignment_endpoints import *
from .user_endpoints import *
from .course_endpoints import *

urlpatterns = [
    path('students', StudentList.as_view()),
    path('students/<int:pk>', StudentDetails.as_view()),
    path('instructors', InstructorList.as_view()),
    path('instructors/<int:pk>', InstructorDetails.as_view()),
    path('admins', AdminList.as_view()),
    path('admins/<int:pk>', AdminDetails.as_view()),
    path('assignments', AssignmentList.as_view()),
    path('assignments/<int:pk>', AssignmentDetails.as_view()),
    path('courses', CourseList.as_view()),
    path('courses/<int:pk>', CourseDetails.as_view())
]