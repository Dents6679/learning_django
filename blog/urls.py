from django.urls import path
from .views import PostListView, PostDetailView
from . import views  # Imports the views module from the current package

urlpatterns = [
    path('', PostListView.as_view(), name='blog-homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # pk is primary key of the class in the db.
    path('about', views.about, name='blog-about'),

]
