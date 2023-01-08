# Generated by Django 4.1.3 on 2023-01-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_jobtechnology_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='offer_compensation',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='offer_range_max',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='offer_range_min',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
