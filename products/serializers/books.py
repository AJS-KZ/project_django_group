from rest_framework import serializers

from products.models import Book


class BookAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    publish_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Book
        fields = 'id', 'title', 'publish_date', 'price'


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = 'title', 'price', 'description'
