"""Define URL patterns for users"""
from learning_log import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
app_name = "users"
urlpatterns = [
    path('login/', 
        LoginView.as_view(template_name='users/login.html'), 
        name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    re_path(r'^register/$', views.register, name='register'),
]
