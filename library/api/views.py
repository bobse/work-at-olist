from django.db.models import Q
from rest_framework import viewsets
from api.models import Book, Author
from api.serializers import AuthorSerializer, BookSerializer


class AuthorView(viewsets.ReadOnlyModelViewSet):
	"""
	    View to list all authors in the DB
	    *Using param `name` it searches for specific authors
	    **Case insensitive search

    """
	serializer_class = AuthorSerializer

	def get_queryset(self):
		queryset = Author.objects.all()
		search_name = self.request.query_params.get('name')
		if search_name:
			queryset = queryset.filter(name__icontains = search_name)
		return queryset


class BookView(viewsets.ModelViewSet):
	"""
		View to list all books in the DB
		*Search available using params:
		`name`, `publication_year`, `edition` or `author`
		**Case insensitive search

	"""

	serializer_class = BookSerializer

	def get_queryset(self):
		queryset = Book.objects.all()

		# Multi-field search
		# __icontains for case-insensitive search
		query = Q()
		if self.request.query_params.get('name'):
			query = query.add(Q(name__icontains = self.request.query_params.get('name')), Q.AND)
		if self.request.query_params.get('edition'):
			query.add(Q(edition = self.request.query_params.get('edition')), Q.AND)
		if self.request.query_params.get('publication_year'):
			query.add(Q(publication_year = self.request.query_params.get('publication_year')), Q.AND)
		if self.request.query_params.get('author'):
			query.add(Q(authors__name__icontains = self.request.query_params.get('author')), Q.AND)

		queryset = queryset.filter(query).distinct().order_by('id')
		return queryset
