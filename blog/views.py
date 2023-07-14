from django.shortcuts import render
from django.views import generic
from blog.models import Blog
from django.urls import reverse_lazy


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailView(generic.DetailView):
    model = Blog


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('header', 'content', 'img')
    success_url = reverse_lazy('blog:blog_list')

