# Generated by Django 4.1.3 on 2022-11-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vezeta', '0007_profile_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='google',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]