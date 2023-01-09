# Generated by Django 4.1.3 on 2023-01-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobtechnology',
            options={'verbose_name_plural': 'Job technologies'},
        ),
        migrations.AddField(
            model_name='joboffer',
            name='offer_compensation',
            field=models.IntegerField(default=0, max_length=6),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='offer_range_max',
            field=models.IntegerField(default=0, max_length=6),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='offer_range_min',
            field=models.IntegerField(default=0, max_length=6),
        ),
    ]