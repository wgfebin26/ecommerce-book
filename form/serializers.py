from rest_framework import serializers
from .models import details

class detailsserializer(serializers.ModelSerializer):
    class Meta:
        model=details
        fields=['id','name','age','email']