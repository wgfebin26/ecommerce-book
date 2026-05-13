from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import media
from .serializers import mediaserializer

@api_view(['GET'])
def media_get(request):
    c=media.objects.all()
    serializer=mediaserializer(c,many=True,context={'request':request})
    return Response(serializer.data)

@api_view(['POST'])
def create_media(request):
    serializer=mediaserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)