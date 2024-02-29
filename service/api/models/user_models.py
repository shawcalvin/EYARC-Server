from django.db import models
from datetime import datetime

class UserStatus(models.Model):
    all_statuses = models.TextChoices("UserStatus", "INACTIVE ACTIVE SUSPENDED")
    status = models.CharField(choices=all_statuses, max_length=20, default="INACTIVE")
    class Meta:
        db_table="user_status"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False)
    user_status_id = models.ForeignKey(UserStatus, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=datetime.now)    
    open_to_research = models.BooleanField(null=True)
    class Meta:
        db_table="student"

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    user_status_id = models.ForeignKey(UserStatus, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=datetime.now)    
    university = models.CharField(max_length=50, null=True)
    class Meta:
        db_table="instructor"

class Admin(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    user_status_id = models.ForeignKey(UserStatus, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table="admin"