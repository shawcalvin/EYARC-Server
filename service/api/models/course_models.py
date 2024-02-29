from django.db import models
from datetime import datetime
from .user_models import Instructor

class Course(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=100)
    class Meta:
        db_table="course"