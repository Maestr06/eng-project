from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import django_filters
from django_filters.views import FilterView
from .filters import PostFilter

@login_required
def dashboard(request):
    filters = Filter.objects.filter(user=request.user)
    applications = Application.objects.filter(user=request.user)
    offers = ''
    try:
        if request.user.company:
            applications = Application.objects.filter(company=request.user.company)
            offers = Offer.objects.filter(offer_company=request.user.company)
    except ObjectDoesNotExist:
        pass
    
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard', 'filters': filters, 'applications': applications, 'offers': offers})

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
            logo = None
            if request.FILES:
                logo = request.FILES['logo']
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            Company.objects.create(user=new_user, company_name=company_name, employee_count=employee_count, address=address, logo=logo)
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
    
class CompanyEditView(View):
    
    def get(self, request):
        user_edit_form = UserEditForm(instance=request.user)
        company_edit_form = CompanyEditForm(instance=request.user.company)
        return render(request, 'account/company_edit.html', {'user_form': user_edit_form, 'company_form': company_edit_form})
    
    def post(self, request):
        user_edit_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        company_edit_form = CompanyEditForm(instance=request.user.company, data=request.POST, files=request.FILES)
        if user_edit_form.is_valid() and company_edit_form.is_valid():
            user_edit_form.save()
            company_edit_form.save()
        return render(request, 'account/company_edit.html', {'user_form': user_edit_form, 'company_form': company_edit_form})

class OfferAddView(View):

    def get(self, request):
        offer_form = OfferForm()
        return render(request, 'account/offer_add.html', {'form': offer_form})

    def post(self, request):
        offer_form = OfferForm(request.POST)
        if offer_form.is_valid():
            new_offer = offer_form.save(commit=False)
            new_offer.offer_company = request.user.company
            new_offer.save()
            new_offer.offer_skills.set(request.POST.getlist('offer_skills'))
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
    
class FilterAddView(View):

    def post(self, request):
        next = request.POST.get('next')
        
        offer_tech = request.POST.get('offer_tech')
        offer_skills = request.POST.get('offer_skills')
        offer_seniority = request.POST.get('offer_seniority')
        offer_location = request.POST.get('offer_location')
        tech = seniority = location = skills = None
        skills = eval(offer_skills)
        if offer_skills:
            skills = [int(i) for i in skills]
            print(skills)
    
        if offer_tech:
            tech = Technology.objects.get(pk=offer_tech)
            # curr_filter.tech = tech
        if offer_seniority:
            seniority = Seniority.objects.get(pk=offer_seniority)
            # curr_filter.seniority = seniority
        if offer_location:
            location = Location.objects.get(pk=offer_location)
            # curr_filter.location = location
        
        test = Filter.objects.filter(user=request.user, tech=tech, seniority=seniority, location=location, skill_query=skills).exists()
        print(test)
        if test == False:
            curr_filter = Filter(user=request.user, tech=tech, seniority=seniority, location=location, skill_query=str(skills))
            curr_filter.save()

        context = {'offer_tech': offer_tech, 'offer_seniority': offer_seniority, 'offer_location': offer_location, 'offer_skills': offer_skills}
        return redirect(next)
    
class CompanyListView(ListView):
    
    model = Company
    paginate_by = 5

    def get_context_data(self, **kwargs: any) -> dict[str, any]: 
        context = super().get_context_data(**kwargs)
        context['section'] = 'companies'
        return context
    
class CompanyDetailView(DetailView):
    
    model = Company

    def get_context_data(self, **kwargs: any) -> dict[str, any]: 
        context = super().get_context_data(**kwargs)
        offers = Offer.objects.filter(offer_company=self.kwargs['pk'])
        context['section'] = 'companies'
        context['offers'] = offers

        return context
    
class ApplicationDetailView(DetailView):
    
    model = Application

    def get_context_data(self, **kwargs: any) -> dict[str, any]: 
        context = super().get_context_data(**kwargs)
        context['section'] = 'applications'
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
        offer = Offer.objects.get(pk=pk)
        company = offer.offer_company
        form = ApplicationForm()
        form.company = company
        form.offer = offer
        return render(request, 'account/offer_apply.html', {'form': form, 'offer_pk': offer_pk, 'company': company})

    def post(self, request, pk):
        form = ApplicationForm(request.POST)
        offer = Offer.objects.get(pk=pk)
        company = offer.offer_company
        # form.company = company
        print(company)
        offer_pk = pk
        errors = ''
        if form.is_valid():
            application = form.save(commit=False)
            application.company = company
            application.offer = offer
            if not request.user.is_anonymous:
            # if user.is_authenticated():
                application.user = request.user
            application.save()
            return redirect('dashboard')
        else:
            errors = form.errors
        return render(request, 'account/offer_apply.html', {'form': form, 'offer_pk': offer_pk, 'company': company, 'errors': errors})
    
class CalculatorView(TemplateView):
    template_name = "account/calculator.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['section'] = 'calculator'
        return context