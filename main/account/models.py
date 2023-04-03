from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    def __str__(self):
        return f'Profile of {self.user.username}'

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    employee_count = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='companies/%Y/%m/%d/',
                              blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name

class Technology(models.Model):
    tech_title = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.tech_title

class Skill(models.Model):
    skill_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill_title

class Offer(models.Model):
    offer_title = models.CharField(max_length=100, default='Oferta pracy')
    offer_tech = models.ForeignKey('Technology', on_delete=models.CASCADE)
    offer_skills = models.ManyToManyField('Skill')
    offer_description = models.CharField(max_length=250, default='Opis oferty pracy')
    offer_post_time = models.DateTimeField(auto_now_add=True)
    offer_range_min = models.PositiveIntegerField(default=0)
    offer_range_max = models.PositiveIntegerField(default=0)
    offer_seniority = models.ForeignKey('Seniority', default=2, on_delete=models.CASCADE)
    offer_location = models.ForeignKey('Location', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.offer_title
    
class Filter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tech = models.ForeignKey('Technology', on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skill')
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    seniority = models.ForeignKey('Seniority', on_delete=models.CASCADE)

class Seniority(models.Model):
    seniority_name = models.CharField(max_length=6)\
    
    class Meta:
        verbose_name_plural = 'Seniorities'

    def __str__(self):
        return self.seniority_name

class Location(models.Model):
    location_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.location_name
    
    
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100) #combine first and last name
    app_text = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    cv = models.BooleanField(default=False)
    applied_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + ' ' + self.offer
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    message_text = models.CharField(max_length=250)
    message_sent_time = models.DateTimeField(auto_now_add=True)
    message_read_time = models.DateTimeField()

    def __str__(self):
        return self.user + ' ' + self.company