from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin  # new
)
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = "book_list" # new
    template_name = "book/book_list.html"
    login_url = "account_login" # new

class BookDetailView(LoginRequiredMixin,
        PermissionRequiredMixin ,DetailView):
    model = Book
    context_object_name = "book" # name
    template_name = "books/book_detail.html"
    login_url = "account_login" # new
    permission_required = "books.special_status"  # new