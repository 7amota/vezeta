# Generated by Django 4.1.3 on 2012-12-31 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vezeta', '0022_rename_realtion_newpost_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpost',
            name='user',
        ),
        migrations.AddField(
            model_name='appointmentdef',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
