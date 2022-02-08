from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment 
from .models import Characters
from .forms import CommentForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
        


class CharacterDetail(View):
    model = Characters
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "characters.html"
