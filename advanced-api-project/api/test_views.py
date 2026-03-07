from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Set up test client
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')

        # Create a test author
        self.author = Author.objects.create(name='Test Author')

        # Create a test book
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2022,
            author=self.author
        )

    # Test retrieving all books (no authentication needed)
    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # Test retrieving a single book (no authentication needed)
    def test_detail_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    # Test creating a book (authenticated users only)
    def test_create_book(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')

    # Test updating a book (authenticated users only)
    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Updated Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.put(f'/api/books/{self.book.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')

    # Test deleting a book (authenticated users only)
    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Test creating a book without authentication (should fail)
    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test filtering books by publication year
    def test_filter_books(self):
        response = self.client.get('/api/books/?publication_year=2022')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # Test searching books by title
    def test_search_books(self):
        response = self.client.get('/api/books/?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # Test ordering books by title
    def test_order_books(self):
        response = self.client.get('/api/books/?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)