from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegistrationForm
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
    return render(request, 'users/profile.html')