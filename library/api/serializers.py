from rest_framework import serializers
from api.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Author
		fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
	# authors = AuthorSerializer(many= True, read_only = True)

	class Meta:
		model = Book
		fields = ['id', 'name', 'edition', 'publication_year', 'authors']
		depth = 1

	def create(self, validated_data):
		parent = super().create(validated_data)
		authors_pk = self.initial_data.get('authors')
		if authors_pk:
			for author in Author.objects.filter(pk__in = authors_pk):
				parent.authors.add(author)
		return parent

	def update(self, instance, validated_data):
		authors_pk = self.initial_data.get('authors')
		parent = super().update(instance, validated_data)
		if authors_pk:
			parent.authors.clear()
			for author in Author.objects.filter(pk__in=authors_pk):
				parent.authors.add(author)
		return parent
