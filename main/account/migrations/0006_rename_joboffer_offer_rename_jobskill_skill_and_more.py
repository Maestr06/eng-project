# Generated by Django 4.1.3 on 2023-03-06 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_joboffer_offer_seniority'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobOffer',
            new_name='Offer',
        ),
        migrations.RenameModel(
            old_name='JobSkill',
            new_name='Skill',
        ),
        migrations.RenameModel(
            old_name='JobTechnology',
            new_name='Technology',
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'Technologies'},
        ),
    ]