from django.test import TestCase
from catalog.models import Author, Book, Genre, Language

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name='Big', last_name='Bob')
        language = Language.objects.create(name = 'test language')
        genre = Genre.objects.create(name = 'test genre')
        
        book = Book.objects.create(
                             title = 'test book',
                             author = author,
                             summary = 'this is a test summary',
                             isbn = 1234567891234,
                             language = language
                             )
        
        book.genre.set([genre])
        
    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'summary')

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'genre')

    def test_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')
