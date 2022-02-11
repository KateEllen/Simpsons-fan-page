from . import views
from django.urls import path
from .views import HomeView, BlogDetailView, AddCommentView, CharacterDetail


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('character/<int:pk>', views.CharacterDetail.as_view(), name='character_detail'),
     path('characters/', views.CharacterList.as_view(), name='characters_list'),
    path('character/<int:pk>/', views.CharacterDetail.as_view(), name='character_detail'),
    path('<pk>/update_character/',
         views.EditCharacterView.as_view(),
         name='update_character'
         ),
    path(
        '<pk>/delete_character/',
        views.DeleteCharacterView.as_view(),
        name='delete_character'
    ),
    path('characters/add/', views.AddCharactersView.as_view(), name="character_add"),

]   
