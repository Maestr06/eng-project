from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Offer, Skill, Technology, Company, Filter, Location, Message, Seniority, Profile


# Define an inline admin descriptor for Company model
# which acts a bit like a singleton
class CompanyInline(admin.StackedInline):
    model = Company
    can_delete = False
    verbose_name_plural = 'Companies'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CompanyInline,)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
    

# Register your models here.
admin.site.register(Technology)
admin.site.register(Skill)
admin.site.register(Offer)
admin.site.register(Company)
admin.site.register(Filter)
admin.site.register(Location)
admin.site.register(Message)
admin.site.register(Seniority)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)