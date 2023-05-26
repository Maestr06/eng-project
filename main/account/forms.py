from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Offer, User, Profile, Company, Application
from django.db import models

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['offer_title', 'offer_tech', 'offer_skills', 'offer_description', 'offer_range_min', 'offer_range_max', 'offer_seniority', 'offer_location']
        widgets = {
            'offer_skills': forms.CheckboxSelectMultiple(),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)    

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data

class CompanyRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = ['company_name', 'employee_count', 'address', 'logo']
        
class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }

class CompanyEditForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['company_name', 'employee_count', 'address', 'logo']

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['app_text', 'email', 'company']

        widgets = {
            'company': forms.HiddenInput,
        }