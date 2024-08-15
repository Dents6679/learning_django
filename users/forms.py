from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
This file is created to add further functionality to the sign up form.
"""

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() # Add an email field

    class Meta:
        """This is a nested namespace for a configuration for the model 
        being effected with this 
        """
        # Specify the Model being used
        model = User
        # specify the fields we want to use, and in what order.
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Check for and remove the unwanted field, replace with actual field name
        if 'usable_password' in self.fields:
            self.fields.pop('usable_password')


