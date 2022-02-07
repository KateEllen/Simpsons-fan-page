from . import views
from django.urls import path
from .views import HomeView, BlogDetailView, AddCommentView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
