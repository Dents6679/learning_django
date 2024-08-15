from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request) -> HttpResponse:
    """
    
    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: _description_
    """
    if request.method == 'POST':  # case for the form being sent.
        form = UserRegistrationForm(request.POST) # Get the form info from the POST request
        if form.is_valid(): # Check The form is valid.
            form.save()  # Save the data to the Database
            username = form.cleaned_data.get('username')  # Get the sanitised input 
            messages.success(request=request, message=f'An account for {username} has been created, please log in.')
            return redirect('login') # URL pattern for homepage 
 
    else: # case for GET.
        form = UserRegistrationForm()


    # this return statement is only reached if errors are found in POST, or if GET is used.
    return render(request=request, template_name='users/register.html', context={'form': form})

    

def logout_view(request)-> HttpResponse:
    logout(request=request)
    return render(request=request, template_name='users/logout.html')


@login_required  # decorator added for login requirement
def profile(request) -> HttpResponse:

    if request.method == 'POST':  # If django is getting this as a post request...
        # Create form object
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # Check the form is valid
        if profile_update_form.is_valid():
            profile_update_form.save()  # save the form.
        messages.success(request=request, message=f'Your profile has been updated.')
        # Do a redirect instead of rendering the template to handle POST-GET redirect issues.

        return redirect('profile')
    else:
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'profile_update_form': profile_update_form
    }

    return render(request, 'users/profile.html', context)