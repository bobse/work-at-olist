from .models import Author, Book
import django_filters


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
            field_name = 'name', lookup_expr = 'icontains')

    class Meta:
        model = Author
        fields = ['name']


class BookFilter(django_filters.FilterSet):
    authors = django_filters.CharFilter(
            field_name = 'authors__name', lookup_expr = 'icontains')
    name = django_filters.CharFilter(
            field_name = 'name', lookup_expr = 'icontains')

    class Meta:
        model = Book
        fields = ['name', 'publication_year', 'edition', 'authors']
