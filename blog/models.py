from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
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
    