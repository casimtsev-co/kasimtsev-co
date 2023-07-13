from django.urls import include, path
from .forms import UserLoginForm
from django.contrib.auth import views as auth_views

from django.contrib.auth import views

urlpatterns = [
    path(
        'login', 
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'),

    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    ]
 
