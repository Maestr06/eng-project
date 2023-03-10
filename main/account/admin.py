from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Offer, Skill, Technology, Company


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CompanyInline(admin.StackedInline):
    model = Company
    can_delete = False
    verbose_name_plural = 'Companies'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CompanyInline,)
    

# Register your models here.
admin.site.register(Technology)
admin.site.register(Skill)
admin.site.register(Offer)
admin.site.register(Company)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)