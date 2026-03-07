from rest_framework import serializers
from .models import Author, Book
from datetime import date

# BookSerializer handles serialization of Book model
# Includes custom validation to ensure publication_year is not in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        # Ensure the publication year is not in the future
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer handles serialization of Author model
# Includes a nested BookSerializer to dynamically serialize related books
# The relationship between Author and Book is handled via the 'books' related_name
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']