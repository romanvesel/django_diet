# Generated by Django 3.1.4 on 2020-12-24 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clever_menu', '0007_auto_20201224_1844'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='day_of_week',
            unique_together={('profile', 'type')},
        ),
    ]
