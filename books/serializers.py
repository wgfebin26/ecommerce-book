from rest_framework import serializers
from .models import category, Book

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields='__all__'



class bookserializer(serializers.ModelSerializer):
    image= serializers.SerializerMethodField()
    class Meta:
        model=Book 
        fields='__all__'
    
    def get_image(self,obj):
        request=self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None




class bookdetailsserializer(serializers.ModelSerializer):
    category=categoryserializer(read_only=True)
    class Meta:
        model=Book 
        fields='__all__'

