# Generated by Django 3.1.5 on 2021-01-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clever_menu', '0017_day_of_week_dishes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day_of_week',
            name='dishes',
        ),
        migrations.AddField(
            model_name='day_of_week',
            name='dishes',
            field=models.ManyToManyField(related_name='dishes', to='clever_menu.Dishes'),
        ),
    ]
