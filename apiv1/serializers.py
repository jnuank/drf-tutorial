from rest_framework import serializers

from shop.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Bookのシリアライザ
    """
    
    class Meta:
        model = Book
        # created_atが要らないのか、省かれている？
        fields = ['id', 'title', 'price']