from django.urls import path

from . import views



urlpatterns = [
    path( '', views.mainPageView.as_view(), name = 'main-page' ),
    path( 'courses', views.coursesView.as_view(), name = 'courses' ),
    path( 'about', views.aboutView, name = 'about' ),
    ]

