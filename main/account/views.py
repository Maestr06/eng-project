from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from .models import Application, Offer, Skill, Technology, Profile, Company
from .forms import ApplicationForm, OfferForm, CompanyRegistrationForm, UserRegistrationForm, UserEditForm, ProfileEditForm, CompanyEditForm
import django_filters
from django_filters.views import FilterView
from .filters import PostFilter

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

class UserRegistrationView(View):

    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})
    
    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
        else:
            return render(request, 'account/register.html', {'user_form': user_form})

class CompanyRegistrationView(View):

    def get(self, request):
        user_form = UserRegistrationForm()
        company_form = CompanyRegistrationForm()
        return render(request, 'account/register_company.html', {'user_form': user_form, 'company_form': company_form})
    
    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        company_form = CompanyRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid() and company_form.is_valid():
            company_name = company_form.cleaned_data['company_name']
            employee_count = company_form.cleaned_data['employee_count']
            address = company_form.cleaned_data['address']
            logo = request.FILES['logo']
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            
            Company.objects.create(user=new_user, company_name=company_name, employee_count=employee_count, address=address, logo=logo)
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
        else:
            return render(request, 'account/register_company.html', {'user_form': user_form, 'company_form': company_form})

class UserEditView(View):

    def get(self, request):
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'account/edit.html', {'user_form': user_edit_form, 'profile_form': profile_edit_form})
    
    def post(self, request):
        user_edit_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_edit_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
        return render(request, 'account/edit.html', {'user_form': user_edit_form, 'profile_form': profile_edit_form})

class OfferAddView(View):

    def get(self, request):
        offer_form = OfferForm()
        return render(request, 'account/offer_add.html', {'form': offer_form})

    def post(self, request):
        offer_form = OfferForm(request.POST)
        if offer_form.is_valid():
            new_offer = offer_form.save(commit=False)
            new_offer.save()
            return redirect('offer_detail', pk=new_offer.pk)
            
class OfferDetailView(DetailView):

    model = Offer

class OfferListView(FilterView):
    
    model = Offer
    paginate_by = 4
    filterset_class = PostFilter
    context_object_name = 'offers'
    template_name = 'account/offer_list.html'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['section'] = 'offers'
        curr_path = self.request.get_full_path()
        curr_path = curr_path[21:]
        if curr_path and len(curr_path) != 44:
            context['path'] = curr_path
        return context
    
    # def get(self, request, *args, **kwargs):
    #     context = super().get(request, *args, **kwargs)
    #     context['path'] = request.get_full_path
    #     return context
    
class FilterAddView(View):

    def get(self, request, path):
        offer_tech = request.GET.get('offer_tech')
        offer_skills = request.GET.get('offer_skills')
        offer_seniority = request.GET.get('offer_seniority')
        offer_location = request.GET.get('offer_location')
        test = request.GET.get('test')
        context = {'offer_tech': offer_tech, 'offer_skills': offer_skills, 'offer_seniority': offer_seniority, 'offer_location': offer_location, 'path': path, 'test': test
        }
        return render(request, 'account/filter_add.html', context)
    
class CompanyListView(ListView):
    
    model = Company
    paginate_by = 5

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['section'] = 'companies'
        return context
    
class ApplicationListView(ListView):
    
    model = Application
    paginate_by = 5

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['section'] = 'applications'
        return context
    
class ApplicationAddView(View):
    def get(self, request, pk):
        offer_pk = pk
        form = ApplicationForm()
        return render(request, 'account/offer_apply.html', {'form': form, 'offer_pk': offer_pk})

    def post(self, request, pk):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
            return redirect('my_applications')

class CalculatorView(TemplateView):
    template_name = "account/calculator.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['section'] = 'calculator'
        return context