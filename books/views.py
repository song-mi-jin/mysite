#from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from books.models import Books

def booklist(request):

    book_list = Books.objects.all()

    context = {'book_list': book_list}
    return render(request, 'books/list.html', context)
