from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# users



class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the blog post.
        content (str): The content of the blog post.
        date_posted (datetime): The date and time when the blog post was created.
        author (User): The author of the blog post.

    """
    title = models.CharField(max_length=100) 
    content = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) # The current time.
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If the user is deleted, delete the post.

    def __str__(self)-> str:
        return str(self.title)


    def get_absolute_url(self):
        """
        This function is called automatically when a post is created. It will redirect the user to the returned URL.
        Gets the absolute url of a post, typically after it has been created.

        Returns: The URL of the post object, as a string

        """
        # build the string to the post-detail URL with keyword argument pk for the post's primary key.
        return reverse('post-detail', kwargs={'pk':self.pk})