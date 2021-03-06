# Generated by Django 3.1.4 on 2020-12-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clever_menu', '0002_auto_20201211_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='kkal_breakfast',
            field=models.IntegerField(default=0, verbose_name='Лимит на завтрак'),
        ),
        migrations.AddField(
            model_name='profile',
            name='kkal_dinner',
            field=models.IntegerField(default=0, verbose_name='Лимит на обед'),
        ),
        migrations.AddField(
            model_name='profile',
            name='kkal_sup',
            field=models.IntegerField(default=0, verbose_name='Лимит на ужин'),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='kind_of_dish',
            field=models.CharField(max_length=100, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='kkal_of_dish',
            field=models.IntegerField(verbose_name='Калорийность'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='kkal_limit_var',
            field=models.CharField(choices=[('1', 'Похудеть'), ('2', 'Сохранить вес'), ('3', 'Набрать вес')], max_length=25, verbose_name='Выбор программы'),
        ),
    ]
