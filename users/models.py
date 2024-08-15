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
        """Uses pillow to resize a provided profile picture upon saving.
        Deletes the told profile picture if a new one is uploaded.

        Returns:
            None
        """

        try:
            # Get the unsaved profile object
            old_profile = Profile.objects.get(pk=self.pk)
            if old_profile.image != self.image:  # Check the image has changed
                # Get the image's path
                old_image_path = old_profile.image.path
                # If the file exists, and it is NOT the default picture, delete the old picture.
                if os.path.isfile(old_image_path) and old_image_path != os.path.join(settings.MEDIA_ROOT, 'default.jpg'):
                    os.remove(old_image_path)
        except Profile.DoesNotExist:
            pass

        # save the parent class.
        super().save(*args, **kwargs)

        # Get the new picture.
        profile_pic = Image.open(self.image.path)

        # If the profile picture is over 256x256, resize it.
        if profile_pic.height > 256 or profile_pic.width > 256:
            # Define desired profile picture size
            output_size = (256, 256)
            # Resize the profile picture
            profile_pic.thumbnail(output_size)
            # Overwrite the profile picture
            profile_pic.save(self.image.path)
