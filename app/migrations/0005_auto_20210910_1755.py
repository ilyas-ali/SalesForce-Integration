# Generated by Django 3.1.1 on 2021-09-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210910_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True, verbose_name='username'),
        ),
    ]
