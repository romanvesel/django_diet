# Generated by Django 3.1.4 on 2020-12-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clever_menu', '0009_auto_20201224_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day_of_week',
            name='dishes',
        ),
        migrations.AddField(
            model_name='day_of_week',
            name='dishes',
            field=models.ManyToManyField(to='clever_menu.Dishes'),
        ),
    ]
