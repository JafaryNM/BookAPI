from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField()
    published_date=serializers.DateField()
    quantity=serializers.IntegerField()
    
    # Method to create book from endpoint
    
    def create(self,data):
        return Book.objects.create(**data) 