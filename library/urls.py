from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path("books/", all_books, name='all_books'),
    path("book_info/<int:id>/", book_info, name='book_detail'),
    path("add_books/", new_book),
    path("book_info/<int:id>/alter_book/", alter_book, name='update_book'),
    path("add_author/", new_author),
    path("add_publisher/", new_publisher),
    path('authorization/', login_func, name='login')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)