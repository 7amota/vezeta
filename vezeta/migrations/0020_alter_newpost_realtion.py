# Generated by Django 4.1.3 on 2022-12-08 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vezeta', '0019_rename_user_newpost_realtion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='realtion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='vezeta.profile'),
        ),
    ]
