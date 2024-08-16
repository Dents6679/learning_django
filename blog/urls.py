from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views  # Imports the views module from the current package

urlpatterns = [
    path('', PostListView.as_view(), name='blog-homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # pk is primary key of the class in the db.
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name='blog-about'),

]
