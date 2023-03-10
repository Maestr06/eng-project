from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    employee_count = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100)

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
    INTERN, JUNIOR, MID, SENIOR = '0', '1', '2', '3'
    LEVELS = [(INTERN, 'Intern'), (JUNIOR, 'Junior'), (MID, 'Mid'), (SENIOR, 'Senior')]
    offer_title = models.CharField(max_length=100, default='Oferta pracy')
    offer_tech = models.ForeignKey('Technology', on_delete=models.CASCADE)
    offer_skills = models.ManyToManyField('Skill')
    offer_description = models.CharField(max_length=250, default='Opis oferty pracy')
    offer_post_time = models.DateTimeField(auto_now_add=True)
    offer_compensation = models.PositiveIntegerField(default=0)
    offer_range_min = models.PositiveIntegerField(default=0)
    offer_range_max = models.PositiveIntegerField(default=0)
    offer_seniority = models.CharField(choices=LEVELS, max_length=6, default=JUNIOR)

    def __str__(self):
        return self.offer_title
