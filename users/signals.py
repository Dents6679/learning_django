from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) -> None:
    """
    A function to create a profile when a user is created.
        Args:
            sender (User): The user model.
            instance (User): The instance of the user model.
            created (bool): A boolean value to check if the user was created.
            kwargs (dict): A dictionary of keyword arguments

        Returns:
            None
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, **kwargs) -> None:
    """
    A function to save a profile when a user is saved.
        Args:
            sender (User): The user model.
            instance (User): The instance of the user model.
            created (bool): A boolean value to check if the user was created.
            kwargs (dict): A dictionary of keyword arguments

        Returns:
            None
    """

    instance.profile.save()


