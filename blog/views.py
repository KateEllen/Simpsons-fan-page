from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Characters
from .forms import CommentForm, CharacterEditForm, CharacterAddForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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


class CharacterList(ListView):
    model = Characters
    queryset = Characters.objects.order_by("name")
    template_name = "character_list.html"
    paginate_by = 6


class CharacterDetail(DetailView):
    model = Characters
    template_name = "character_detail.html"


@method_decorator(login_required(
    login_url='/accounts/login/'), name='dispatch')
class EditCharacterView(UpdateView):
    model = Characters
    form_class = CharacterEditForm
    template_name = 'edit_character.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy("character_detail", args=[str(self.object.pk)])


@method_decorator(login_required(
    login_url='/accounts/login/'), name='dispatch')
class DeleteCharacterView(DeleteView):
    model = Characters
    template_name = 'delete_character.html'
    success_url = reverse_lazy('character_list')


@method_decorator(login_required(
    login_url='/accounts/login/'), name='dispatch')
class AddCharactersView(CreateView):
    model = Characters
    form_class = CharacterAddForm
    template_name = 'add_characters.html'
    success_url = reverse_lazy('character_list')


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))

# @login_required

# class EditComment(UpdateView):
#     def edit_comment(self, request, comment_id):
#         """ Edit Comment """
#         """ Prefill Form """
#         comment = get_object_or_404(Comment, pk=comment_id)
#         if request.user == comment.comment_author or request.user.is_superuser:
#             if request.method == 'POST':
#                 comment_form = CommentForm(request.POST, instance=comment)
#                 if comment_form.is_valid():
#                     comment_form.save()
#                     messages.success(request, 'Comment successfully updated')
#                     return redirect(reverse('blog_detail', args=[comment.post]))
#                 else:
#                     messages.error(request,
#                                 'Error - Please check form is valid and \
#                                         try again.')
#             else:
#                 comment_form = CommentForm(instance=comment)
#                 messages.info(request, f'You are editing {comment.comment_title}')
#         else:
#             messages.error(request, 'Sorry, only the comment author can do that')
#             return redirect(reverse('home'))

#         template = 'explore/edit_comment.html'
#         context = {
#             'comment_form': comment_form,
#             'comment': comment,
#             'on_profile_page': True
#         }

#         return render(request, template, context)

# @login_required
# def delete_comment(request, comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user == comment.comment_author or request.user.is_superuser:
#         """ Delete Comment """
#         comment.delete()
#         messages.success(request, 'Comment deleted')
#         return redirect(reverse('view_explore'))
#     else:
#         messages.error(request, 'Sorry, only the comment author can do that')
#         return redirect(reverse('home'))
