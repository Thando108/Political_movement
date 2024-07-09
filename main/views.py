from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

def home(request):
    """
    View for the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home.html template.
    """
    return render(request, 'main/home.html')

def mission(request):
    """
    View for the mission page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered mission.html template.
    """
    return render(request, 'main/mission.html')

def issues(request):
    """
    View for listing all issues.

    Fetches all issues with a publication date less than or equal to the current time
    and orders them by publication date in descending order.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered issues.html template with the fetched issues.
    """
    issues = Issue.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'main/issues.html', {'issues': issues})

def issue_detail(request, issue_id):
    """
    View for a detailed issue page.

    Fetches the issue by its primary key (ID), or returns a 404 error if not found.

    Args:
        request: The HTTP request object.
        issue_id (int): The ID of the issue to fetch.

    Returns:
        HttpResponse: The rendered issue_detail.html template with the fetched issue.
    """
    issue = get_object_or_404(Issue, pk=issue_id)
    return render(request, 'main/issue_detail.html', {'issue': issue})

def contribute(request):
    """
    View for the contribute page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered contribute.html template.
    """
    return render(request, 'main/contribute.html')

def register(request):
    """
    View for the user registration page.

    If the request method is POST, creates a form instance with the submitted data,
    validates and saves the new user to the database, authenticates and logs in the user,
    and redirects to the home page (or any other desired URL).
    If the request method is not POST, creates an empty form instance.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered register.html template with the form.
        HttpResponseRedirect: Redirects to the home page after successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def subscribe(request):
    """
    View for the subscribe page.

    If the request method is POST, retrieves the email from the submitted data
    and handles the email logic (e.g., save to the database, send a confirmation email, etc.).
    If the request method is not POST, redirects to the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A thank you message after successful subscription.
        HttpResponseRedirect: Redirects to the home page if the request method is not POST.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        return HttpResponse(f'Thank you for subscribing with {email}!')
    return redirect('home')

