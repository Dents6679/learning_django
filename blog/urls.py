from django.urls import path
from . import views  # Imports the views module from the current package

urlpatterns = [
    path('', views.homepage, name='blog-homepage'),
    path('about', views.about, name='blog-about'),

]
