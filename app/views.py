from rest_framework import generics
from .models import Author, Book, BookReview,AuthorReview
from .serializers import AuthorSerializer, BookSerializer, AuthorReviewSerializer,BookReviewSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookReviewView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer

class AuthorReviewListView(generics.ListCreateAPIView):
    queryset = AuthorReview.objects.all()
    serializer_class = AuthorReviewSerializer
