from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import details
from .serializers import detailsserializer

@api_view(['GET'])
def get_details(request):
    users=details.objects.all()
    serializer=detailsserializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def enter_details(request):
    email=request.data.get('email')
    password=request.data.get('password')
    confirmpassword=request.data.get('confirmpassword')

    serializer=detailsserializer(data=request.data)
    if details.objects.filter(email=email).exists():
        return Response({'message':'email already exists'},status=status.HTTP_400_BAD_REQUEST)
    if password!=confirmpassword:
        return Response({'message':'password incorrct'},status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_det(requset):
    email=requset.data.get('email')
    password=requset.data.get('password')

    if details.objects.filter(email=email).exists():
        c=details.objects.filter(email=email).first()
        if password==c.password:
            return Response({'message':'login successfully'},status=status.HTTP_200_OK)
        return Response({'message':'incorrect password'},status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'email doesnt exists'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_id(request,pk):
    d=details.objects.get(pk=pk)
    serializer=detailsserializer(d)
    return Response(serializer.data)