from django.urls import path, include
from api.views import AuthorView, BookView
from rest_framework.routers import DefaultRouter

app_name = 'api'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BookView, basename="books")
router.register(r'authors', AuthorView, basename="authors")


urlpatterns = [
    # path('authors/', AuthorView.as_view(), name='authors'),
	path('', include(router.urls))
]
