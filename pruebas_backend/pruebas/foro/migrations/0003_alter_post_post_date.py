# Generated by Django 3.2.3 on 2021-12-10 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0002_auto_20211210_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]