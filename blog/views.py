from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create views here.

def homepage(request) -> HttpResponse:
    """Bound function for the blog's homepage.

    Args:
        request (HttpRequest): The HTTP request to view the page.

    Returns:
        HttpResponse: Returns the homepage.
    """

    # create a dictionary of data within the function scope to pass to the render fn. 
    homepage_context = {
        'posts' : Post.objects.all() # Query the database for all posts.
    }

    # Fill and render the page into a HttpResponse
    response: HttpResponse = render(request=request,
                                    template_name='blog/homepage.html',
                                    context=homepage_context)

    return response



def about(request) -> HttpResponse:
    """Bound function for the blog's about page.

    Args:
        request (_type_): _description_

    Returns:
        HttpResponse: _description_
    """
    response: HttpResponse = render(request=request, template_name='blog/about.html')

    return response
