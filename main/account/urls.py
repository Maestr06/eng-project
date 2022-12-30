from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import UserLoginView

urlpatterns = [
    # login / logout urls with Django ootb views
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
]
