from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import category ,Book
from .serializers import categoryserializer ,bookserializer,bookdetailsserializer

@api_view(['GET'])
def get_cetegory(request):
    users=category.objects.all()
   
    serializer=categoryserializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_cetegory(request):
    name=request.data.get('name')
    serializer=categoryserializer(data=request.data)
    if category.objects.filter(name=name).exists():
        return Response({'message':'name already exists'},status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_cetegory(request,pk):
    product=category.objects.get(pk=pk)
    serializer=categoryserializer(product,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'books updates'},status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_cetegory_byid(request,pk):
    product=category.objects.get(pk=pk)
    serializer=categoryserializer(product)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_cetegory(request,pk):
    product=category.objects.get(pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#books

@api_view(['GET'])
def get_books(request):
    b=Book.objects.all()
    a=request.query_params.get('catID')
    d=request.query_params.get('bname')
    y=request.query_params.get('gtprice')
    mini=request.query_params.get('mini')
    maxi=request.query_params.get('maxi')

    if a:
        b=Book.objects.filter(category_id__id=a)
    if d:     
        b=Book.objects.filter(bookname__exact=d)
    if y:
        b=Book.objects.filter(price__gt=y)
    if mini and maxi:
        b=Book.objects.filter(price__range=[mini,maxi])

    serializer=bookdetailsserializer(b,many=True,context={'request':request})
    return Response(serializer.data)

@api_view(['POST'])
def add_books(request):
    serializer=bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_books(request,pk):
    c=Book.objects.get(pk=pk)
    serializer=bookserializer(c,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'books updated'},status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book_id(request,pk):
    d=Book.objects.get(pk=pk)
    serializer=bookserializer(d)
    return Response(serializer.data)

@api_view(['DELETE'])
def del_books(request,pk):
    m=Book.objects.get(pk=pk)
    m.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)   