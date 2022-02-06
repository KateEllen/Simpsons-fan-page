from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class HomeView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'
