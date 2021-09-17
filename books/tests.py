from django.test import TestCase

# Create your tests here.
from books.models import Books

class BooksTestCase(TestCase):
    def setUp(self):
        Books.objects.create(book_name="lion", book_writer="roar")
        Books.objects.create(book_name="cat", book_writer="meow")

    def test_books_name(self):

        book1 = Books.objects.get(book_name="lion")
        book2 = Books.objects.get(book_name="cat")
        self.assertEqual(book1.name(), 'lion')
        self.assertEqual(book2.name(), 'cat')
