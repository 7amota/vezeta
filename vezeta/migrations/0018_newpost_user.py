# Generated by Django 4.1.3 on 2022-12-08 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vezeta', '0017_appointmentdef'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpost',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vezeta.profile'),
            preserve_default=False,
        ),
    ]
