from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [
    # login / logout urls with Django ootb views
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register_company/', CompanyRegistrationView.as_view(), name='register_company'),
    path('offer/<int:pk>/', OfferDetailView.as_view(), name='offer_detail'),
    path('offer/add/', login_required(OfferAddView.as_view()), name='offer_add'),
    path('offer/list/', OfferListView.as_view(), name='offer_list' ),
    path('edit/user/', UserEditView.as_view(), name='edit_user'),
    path('edit/company/', CompanyEditView.as_view(), name='edit_company'),
    path('offer/<int:pk>/apply/', ApplicationAddView.as_view(), name='offer_apply'),
    path('my_applications/', ApplicationListView.as_view(), name='my_applications'),
    path('calculator/', CalculatorView.as_view(), name='calculator'),
    path('companies/', CompanyListView.as_view(), name='companies'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('filter/add/', FilterAddView.as_view(), name='filter_add')
]
