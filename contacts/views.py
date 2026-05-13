from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import contact
from .serializers import contactserializer
from infos.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random

@api_view(['GET'])
def get_contacts(request):
    c=contact.objects.all()
    serializer=contactserializer(c,many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def create_contacts(request):
#     serializer=contactserializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_contacts(request):
    email=request.data.get('email')
    name=request.data.get('name')

    import random
    def username(name):
        d=""
        for i in range (3):
            numbers=random.randint(0,9)
            d+=str(numbers)
        return f"{name}@{d}"
    user=name
    result=username(user)
    print("password is :",result)
    

    serializer=contactserializer(data=request.data)
    if serializer.is_valid():
        subject="Welcome to Alo Infotech – You're In!"
        message=f"Hi {name},Thanks for subscribing to Alo Infotech news_letter! and your OTP is {result}"
        recipient_list=[email]
        send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently=False)
        serializer.save()
        return Response({'message': 'Contact created', 'Contact': serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
