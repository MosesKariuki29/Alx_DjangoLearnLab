"""
Sample ORM Queries for relationship_app
"""

import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# ---------------------------------------------------
# Query 1: Get all books by a specific author
# ---------------------------------------------------
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()


# ---------------------------------------------------
# Query 2: List all books in a specific library
# ---------------------------------------------------
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# ---------------------------------------------------
# Query 3: Retrieve the librarian for a library
# ---------------------------------------------------
def get_librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


# Example usage (only runs if file executed directly)
if __name__ == "__main__":
    print("Sample queries loaded successfully.")
