from django.db import models
from datetime import datetime
from .user_models import Student, Instructor
from .course_models import Course
from .assignment_models import Assignment

class CourseStudent(models.Model):
    date_student_was_added = models.DateTimeField(default=datetime.now)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        db_table="course_student"
        
class StudentCourseAssignment(models.Model):
    date_assignment_was_assigned = models.DateTimeField(default=datetime.now)
    date_completed = models.DateTimeField(null=True)
    date_due = models.DateTimeField(null=True)
    date_started = models.DateTimeField(null=True)
    is_for_grade = models.BooleanField(null=True)
    grade = models.FloatField(null=True)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.RESTRICT)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    class Meta:
        db_table="student_course_assignment"