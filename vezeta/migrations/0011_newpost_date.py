# Generated by Django 4.1.3 on 2022-11-20 03:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vezeta', '0010_newpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]