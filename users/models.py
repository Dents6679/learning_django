from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
import os

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='Hello! I am a new user.')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):

        # Check if the instance already exists in the database
        try:
            # Get the 'old' already saved instance of the profile object
            old_instance = Profile.objects.get(pk=self.pk)
            # Get the image path from that old instance
            old_image_path = old_instance.image.path
        except Profile.DoesNotExist:
            old_instance = None
            old_image_path = None

        # Save the instance to the database
        super().save(*args, **kwargs)

        # Custom logic after saving, to resize the image.
        img_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        try:
            profile_pic = Image.open(img_path)
            # If the profile picture is over 256x256, resize it.
            if profile_pic.height > 256 or profile_pic.width > 256:
                # Define desired profile picture size
                output_size = (256, 256)
                # Resize the profile picture
                profile_pic.thumbnail(output_size)
                # Overwrite the profile picture
                profile_pic.save(self.image.path)
        except FileNotFoundError as e:
            print("Error occurred while reading profile picture.")

            print(e)

        # Delete the old image if it exists and is not the default image.
        if old_instance and old_image_path != self.image.path and 'default.jpg' not in old_image_path:
            if os.path.exists(old_image_path):
                os.remove(old_image_path)