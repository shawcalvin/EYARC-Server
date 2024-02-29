from django.db import models
from datetime import datetime

class AssignmentDifficulty(models.Model):
    all_difficulties = models.TextChoices("AssignDifficulties", "EASY INTERMEDIATE DIFFICULT NONE")
    difficulty = models.CharField(choices=all_difficulties, max_length=20, default="NONE")
    class Meta:
        db_table="assignment_difficulty"
        
class AssignmentTopic(models.Model):
    topic = models.CharField(max_length=100)
    class Meta:
        db_table="assignment_topic"
        
class Assignment(models.Model):
    instruction = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    estimated_duration = models.FloatField(null=True)
    assignment_topic = models.ForeignKey(AssignmentTopic, null=True, on_delete=models.SET_NULL)
    assignment_difficulty = models.ForeignKey(AssignmentDifficulty, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=datetime.now)
    is_required = models.BooleanField(null=True)
    class Meta:
        db_table="assignment"

class Question(models.Model):
    question = models.TextField()
    question_num = models.IntegerField(null=True)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    class Meta:
        db_table="question"