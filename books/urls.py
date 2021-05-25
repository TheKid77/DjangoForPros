  
from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView
from .views import add_book, add_review, edit_book, delete_book, delete_review


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
     # Page for adding a new book
    path('add_book/', add_book, name='add_book'),
     # Page for editing a book
    path('edit_book/<uuid:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<uuid:book_id>/', delete_book, name='delete_book'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
     # Page for adding a review
    path('add_review/', add_review, name='add_review'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'), 
]