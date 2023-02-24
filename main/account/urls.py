from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import UserRegistrationView, AddOfferView

urlpatterns = [
    # login / logout urls with Django ootb views
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('offer/add/', login_required(AddOfferView.as_view()), name='addoffer')
]
