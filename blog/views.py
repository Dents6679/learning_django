from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
                                    template_name='blog/post_list.html',
                                    context=homepage_context)

    return response

class PostListView(ListView):
    """Class to view all posts as a list, in reverse order.
    """
    # Set the model to use from the view. This supplies all instances of the class to the template as an iterable list.
    # This list is passed to the template with the name 'object_list'.
    model = Post
    # Reverse the ordering
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    """Class to view all posts as a list, in reverse order.
    """
    # Set the model to use from the view. This supplies all instances of the class to the template as an iterable list.
    # This list is passed to the template with the name 'object_list'.
    template_name = 'blog/user_posts.html'
    model = Post
    # Reverse the ordering
    ordering = ['-date_posted']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['user'] = user
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    """Class to view a post in Detail.
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Class to create a post.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """Sets the author of a created post before validating it.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Class to update a post
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """Sets the author of a created post before validating it.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Test if the user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Class to view a post in Detail.
    """
    model = Post
    success_url = '/'
    def test_func(self):
        """Test if the user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author



def about(request) -> HttpResponse:
    """Bound function for the blog's about page.
    """
    response: HttpResponse = render(request=request, template_name='blog/about.html')

    return response
