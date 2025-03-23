from rest_framework import serializers
from .models import TraineeProfile

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraineeProfile    
        fields = '__all__'