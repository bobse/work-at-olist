from rest_framework import generics
from rest_framework import viewsets

from api.models import Book, Author
from api.serializers import AuthorSerializer, BookSerializer


class AuthorView(viewsets.ReadOnlyModelViewSet):
	"""
	    View to list all authors in the DB ordered by Name
	    *Using param name it searches for specific authors
	    **Case insensitive search

    """
	serializer_class = AuthorSerializer

	def get_queryset(self):
		"""
		Optionally searches the authors by name,
		by filtering against a `name` query parameter in the URL.
		"""
		queryset = Author.objects.all()
		search_name = self.request.query_params.get('name')
		if search_name is not None:
			queryset = queryset.filter(name__icontains = search_name)
		return queryset


class BookView(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
