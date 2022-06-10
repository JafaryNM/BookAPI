from django.shortcuts import render
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import BookSerializer

# Create your views here.

############## ENDPOINT TO RETRIVE ALL DATA FROM DATABASE #################################
@api_view(['GET'])
def book_list(request):
    books=Book.objects.all()
    serializer=BookSerializer(books, many=True)
    return Response(serializer.data)

################### ENDPOINT T0 ADD ALL DATA IN DATABASE ###################################
@api_view(['POST'])
def book_create(request):
    serializer=BookSerializer(data=request.data)
    # Validate serializer data
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)   








