from django.db import models
from django.contrib.auth.models import User
class Present_Book(models.Model):
    isbn = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    book_link = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=20, default='present')
    comment = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.title

class Request_Book(models.Model):
    isbn = models.IntegerField('isbn_code here')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    book_link = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField('date published')
    attribute = models.CharField(max_length=20, default='request')
    comment = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.title
# Create your models here.
