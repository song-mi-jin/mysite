from django.urls import path
from books.views import *

app_name = 'books'
urlpatterns = [
    path('', booklist, name='list'),

]
