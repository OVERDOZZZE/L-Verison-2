from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path("books/", books, name='all_books'),
    path("book_info/<int:id>/", book_detail, name='book_detail'),
    path("add_books/", add_book),
    path("book_info/<int:id>/alter_book/", update_book, name='update_book'),
    path("add_author/", add_author),
    path("add_publisher/", add_publisher),
    path('authorization/', login_view, name='login')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
