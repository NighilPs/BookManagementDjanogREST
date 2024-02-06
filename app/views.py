from rest_framework import generics,permissions
from .models import Author, Book, BookReview,AuthorReview
from .serializers import AuthorSerializer, BookSerializer, AuthorReviewSerializer,BookReviewSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookReviewView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorReviewListView(generics.ListCreateAPIView):
    queryset = AuthorReview.objects.all()
    serializer_class = AuthorReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
