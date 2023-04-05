from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Book

class BookListView(ListView):
    model = Book
    context_object_name = "book_list" # new
    template_name = "book/book_list.html"

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book" # name
    template_name = "books/book_detail.html"
