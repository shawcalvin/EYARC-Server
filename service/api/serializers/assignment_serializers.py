from rest_framework import serializers
from ..models.assignment_models import *

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'