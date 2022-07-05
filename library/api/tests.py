from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api.models import Book, Author
from django.core.management import call_command
import csv
import os


class AuthorTest(APITestCase):
    def test_import_authors_command(self):
        """
            Creates a .csv file, import a file, checks if is successful.
        """
        authors = [['name']]
        authors.extend([[f'Author {n}'] for n in range(1, 50)])
        filename = 'test_authors.csv'
        with open('test_authors.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(authors)
        call_command('import_authors', filename)
        os.remove(filename)
        authors = Author.objects.all()
        self.assertEqual(Author.objects.count(), len(authors))

    def test_author_get_list(self):
        """
            GET authors list
        """
        url = reverse('api:authors-list')
        Author.objects.create(name="Test Author")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(response.data.get('results')[0].get('name'), 'Test Author')

    def test_author_details(self):
        """
            GET author details
        """
        author = Author.objects.create(name="Test Author")
        url = f"{reverse('api:authors-list')}{author.id}/"
        response = self.client.get(url, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), author.name )

    def test_author_search_name(self):
        """
            SEARCH author by name
        """
        Author.objects.create(name="Test Author")
        Author.objects.create(name = "Test Author 2")
        url = reverse('api:authors-list')
        data = {'name': '2'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)


class BookTest(APITestCase):
    def setUp(self):
        self.data = [
                {'name': 'Test Book', 'edition': 1, 'publication_year': 1},
                {'name': 'Test Book 2', 'edition': 2, 'publication_year': 3},
                {'name': 'Test Book 3', 'edition': 3, 'publication_year': 3}
        ]

    def _create_book(self):
        book_ids = []
        for idx, value in enumerate(self.data):
            b = Book.objects.create(**value)
            b.authors.add(Author.objects.create(name = f'Author {idx}'))
            book_ids.append(b.id)
        return book_ids

    def test_book_post_without_authors(self):
        """
            POST
            Creates a book object by post request. Without authors.
        """
        url = reverse('api:books-list')
        response = self.client.post(url, self.data[0], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.filter().values().first()
        book.pop('id')
        self.assertEqual(book, self.data[0])

    def test_book_post_with_authors(self):
        """
            POST
            Creates a book object by post request.
            **WITH authors.
        """
        url = reverse('api:books-list')
        data_with_author = self.data[0].copy()
        author = Author.objects.create(name = f'Author 1')
        data_with_author['authors'] = [author.id]

        response = self.client.post(url, data_with_author, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.get()
        self.assertEqual(list(book.authors.values_list('id', flat= True)), data_with_author['authors'])

    def test_book_get(self):
        """
            GET book list request
        """
        url = reverse('api:books-list')
        self._create_book()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), len(self.data))

    def test_book_search_name(self):
        """
	        SEARCH book by name
        """
        url = reverse('api:books-list')
        self._create_book()
        data = {'name': '2'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)

    def test_book_search_author(self):
        """
	        SEARCH book by author
        """
        url = reverse('api:books-list')
        self._create_book()
        data = {'authors': '1'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)

    def test_book_details(self):
        """
	        GET book details
        """
        book_ids = self._create_book()
        url = f"{reverse('api:books-list')}{book_ids[0]}/"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), Book.objects.get(pk=book_ids[0]).name)

    def test_book_delete(self):
        """
	        DELETE a book
        """
        book_ids = self._create_book()
        url = f"{reverse('api:books-list')}{book_ids[0]}/"
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), len(book_ids)-1)

    def test_book_update_put(self):
        """
	        Updates a book using PUT
        """
        book_ids = self._create_book()
        url = f"{reverse('api:books-list')}{book_ids[0]}/"
        new_data = self.data[0].copy()
        new_data['name'] = 'new name'
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=book_ids[0]).name, new_data['name'])

    def test_book_update_patch(self):
        """
	        Updates a book using PATCH
        """
        book_ids = self._create_book()
        url = f"{reverse('api:books-list')}{book_ids[0]}/"
        new_data = {'name': 'new name'}
        response = self.client.patch(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=book_ids[0]).name, new_data['name'])
