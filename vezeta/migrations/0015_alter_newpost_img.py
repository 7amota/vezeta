# Generated by Django 4.1.3 on 2022-11-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vezeta', '0014_alter_newpost_plugin_alter_newpost_title_plugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='cats/%y/%m/%d', verbose_name='صورة للمقال'),
        ),
    ]