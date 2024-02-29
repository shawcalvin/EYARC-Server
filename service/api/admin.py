from django.contrib import admin
from .models.assignment_models import Assignment, AssignmentDifficulty, AssignmentTopic
from .models.user_models import Student, Instructor, Admin, UserStatus
from .models.course_models import Course

admin.site.register(Assignment)
admin.site.register(AssignmentDifficulty)
admin.site.register(AssignmentTopic)
admin.site.register(UserStatus)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Admin)
admin.site.register(Course)