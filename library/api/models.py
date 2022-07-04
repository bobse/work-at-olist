from django.db import models


class Author(models.Model):
	name = models.CharField(max_length = 200, blank = False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Book(models.Model):
	name = models.CharField(max_length = 200, blank = False)
	edition = models.PositiveIntegerField()
	publication_year = models.PositiveIntegerField()
	authors = models.ManyToManyField(Author,
	                                 related_name = "books",
	                                 through = "BookAuthor")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class BookAuthor(models.Model):
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	author = models.ForeignKey(Author, on_delete = models.CASCADE)

	def __str__(self):
		return f"{self.book.__str__()}, {self.author.__str__()}"
