# Generated by Django 3.1.1 on 2021-09-10 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210910_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='company',
            new_name='phone',
        ),
    ]
