from django.urls import path
from app.views import AuthorListCreateView, BookListCreateView, BookReviewView, AuthorReviewListView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/reviews/', BookReviewView.as_view(), name='review-create'),
    path('authors/reviews/', AuthorReviewListView.as_view(), name='author-reviews'),
]
