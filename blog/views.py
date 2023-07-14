from django.shortcuts import render
from django.views import generic
from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('header', 'content', 'img', 'date')