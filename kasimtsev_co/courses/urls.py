from django.urls import path

from . import views



urlpatterns = [
    path( '', views.mainPageView.as_view(), name = 'main-page' ),
    path( 'course', views.courseView.as_view(), name = 'course' ),
    path( 'course/enrole', views.courseEnroleView, name = 'course-enrole' ),
    path( 'about', views.aboutView, name = 'about' ),
    ]

