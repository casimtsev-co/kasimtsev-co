from django.urls import include, path
from .forms import UserLoginForm
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path(
        'login', 
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('signup', views.StudentRegistrationView, name = 'signup' ),
    path('password-reset', auth_views.LogoutView.as_view(), name='password-reset'),
    ]
 
