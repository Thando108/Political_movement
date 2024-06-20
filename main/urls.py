# main/urls.py

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# Define the app name for namespacing the URLs
app_name = 'main'

# List of URL patterns for the application
urlpatterns = [
    # URL pattern for the home page, mapped to the home view
    path('', views.home, name='home'),
    
    # URL pattern for the mission page, mapped to the mission view
    path('mission/', views.mission, name='mission'),
    
    # URL pattern for the list of issues, mapped to the issues view
    path('issues/', views.issues, name='issues'),
    
    # URL pattern for the issue detail page, mapped to the issue_detail view
    # The issue_id parameter is passed to the view
    path('issues/<int:issue_id>/', views.issue_detail, name='issue_detail'),
    
    # URL pattern for the contribute page, mapped to the contribute view
    path('contribute/', views.contribute, name='contribute'),
    
    # URL pattern for the login page, using Django's built-in LoginView
    # The template used for rendering the login page is specified
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    
    # URL pattern for the logout functionality, using Django's built-in LogoutView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # URL pattern for the registration page, mapped to the register view
    path('register/', views.register, name='register'),
    
    # URL pattern for the subscribe functionality, mapped to the subscribe view
    path('subscribe/', views.subscribe, name='subscribe'),
]
