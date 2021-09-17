from django.db import models
from django.utils import timezone

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=200, unique=True)
    book_writer = models.CharField(max_length=200)
    book_date = models.DateField(default=timezone.now)
    book_pay = models.IntegerField(default=0)
    book_oview = models.TextField(null=True,default='')

    def __str__(self):
        return "도서명 : " +self.book_name

    def name(self):
        return self.book_name
