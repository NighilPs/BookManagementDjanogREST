# book_management/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    total_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    total_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.FloatField()
    comment = models.TextField()

    def save(self, *args, **kwargs):
        if self.book:
            self.book.total_rating += self.rating
            self.book.save()
        super().save(*args, **kwargs)

class AuthorReview(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.FloatField()
    comment = models.TextField()

    def save(self, *args, **kwargs):
        if self.author:
            self.author.total_rating += self.rating
            self.author.save()
    
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comment
