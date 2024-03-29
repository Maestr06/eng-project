# Generated by Django 4.1.3 on 2023-04-19 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('employee_count', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to='companies/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seniority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seniority_name', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name_plural': 'Seniorities',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_title', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_title', models.CharField(default='Oferta pracy', max_length=100)),
                ('offer_description', models.CharField(default='Opis oferty pracy', max_length=250)),
                ('offer_post_time', models.DateTimeField(auto_now_add=True)),
                ('offer_range_min', models.PositiveIntegerField(default=0)),
                ('offer_range_max', models.PositiveIntegerField(default=0)),
                ('offer_location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.location')),
                ('offer_seniority', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.seniority')),
                ('offer_skills', models.ManyToManyField(to='account.skill')),
                ('offer_tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.technology')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=250)),
                ('message_sent_time', models.DateTimeField(auto_now_add=True)),
                ('message_read_time', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.location')),
                ('seniority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.seniority')),
                ('skills', models.ManyToManyField(to='account.skill')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.technology')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('app_text', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('cv', models.BooleanField(default=False)),
                ('applied_time', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
