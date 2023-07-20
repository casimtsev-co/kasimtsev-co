from django.urls import path

from . import views



urlpatterns = [
    path( '', views.mainPageView.as_view(), name = 'main-page' ),
    path( 'course', views.courseView.as_view(), name = 'course' ),
    path( 'about', views.aboutView, name = 'about' ),
    path( 'course/enrole', views.courseEnroleView, name = 'course-enrole' ),
    path( 'course/enrole/succesfull', views.successEnroleView, name = 'enrole-success' ),
    path( 'course/enrole/error', views.errorEnroleView, name = 'enrole-error' ),
    path( 'course/table', views.tableOfCourse, name = 'table-of-contents' ),
    ]

