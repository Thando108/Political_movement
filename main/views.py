# main/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# View for the home page
def home(request):
    # Renders the home.html template
    return render(request, 'main/home.html')

# View for the mission page
def mission(request):
    # Renders the mission.html template
    return render(request, 'main/mission.html')

# View for listing all issues
def issues(request):
    # Fetches all issues with a publication date less than or equal to the current time
    # and orders them by publication date in descending order
    issues = Issue.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    # Renders the issues.html template with the fetched issues
    return render(request, 'main/issues.html', {'issues': issues})

# View for a detailed issue page
def issue_detail(request, issue_id):
    # Fetches the issue by its primary key (ID), or returns a 404 error if not found
    issue = get_object_or_404(Issue, pk=issue_id)
    # Renders the issue_detail.html template with the fetched issue
    return render(request, 'main/issue_detail.html', {'issue': issue})

# View for the contribute page
def contribute(request):
    # Renders the contribute.html template
    return render(request, 'main/contribute.html')

# View for the user registration page
def register(request):
    if request.method == 'POST':
        # If the request method is POST, create a form instance with the submitted data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the new user to the database
            form.save()
            # Retrieve the username and password from the form
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate the new user
            user = authenticate(username=username, password=raw_password)
            # Log the user in
            login(request, user)
            # Redirect to the home page (or any other desired URL)
            return redirect('main:home')  # Replace 'home' with your desired redirect URL
    else:
        # If the request method is not POST, create an empty form instance
        form = UserCreationForm()
    # Renders the register.html template with the form
    return render(request, 'main/register.html', {'form': form})

# View for the subscribe page
def subscribe(request):
    if request.method == 'POST':
        # If the request method is POST, retrieve the email from the submitted data
        email = request.POST.get('email')
        # Handle the email logic here, e.g., save to the database, send a confirmation email, etc.
        return HttpResponse(f'Thank you for subscribing with {email}!')
    # If the request method is not POST, redirect to the home page
    return redirect('home')

