from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django_registration.signals import user_registered, user_activated
from django.contrib import auth
from django.dispatch import receiver
from django.shortcuts import redirect
from random import randint


def user_created(sender, user, request, **kwargs):
    profile = Profile(user=user, email=user.email, name=user)
    profile.save()
    min_id = Dishes.objects.order_by('id')[0].id
    for i in DAYS_OF_WEEK:
        day = Day_of_week(profile=profile, type=int(i[0]))
        day.save()
        dishes = []
        while len(dishes) < 3:
            dish = Dishes.objects.get(id=randint(min_id, min_id + Dishes.objects.count() - 1))
            if dish not in dishes:
                dishes.append(dish)
        day.dishes.add(*dishes)


def login_on_activation(sender, user, request, **kwargs):
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    return redirect('profile', pk=request.user.pk)


user_activated.connect(login_on_activation)
user_registered.connect(user_created)


class Dishes(models.Model):
    name = models.CharField('Название', max_length=100)
    kkal_of_dish = models.IntegerField('Калорийность')
    compose = models.TextField('Состав', )
    recipe = models.TextField('Рецепт', )
    kind_of_dish = models.CharField('Вид', max_length=100)
    img = models.ImageField('Фото', upload_to='gallery')

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return f'{self.name} - {self.pk}'


TYPE_LIMIT = (
    ('1', _('Похудеть')),
    ('2', _('Сохранить вес')),
    ('3', _('Набрать вес')),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    name = models.CharField('Имя', max_length=100)
    age = models.IntegerField('Возраст', default=0)
    height = models.IntegerField('Рост', default=0)
    weight = models.IntegerField('Вес', default=0)
    kkal = models.IntegerField('Расход калорий', default=0)
    kkal_limit_var = models.CharField('Выбор программы', max_length=25, choices=TYPE_LIMIT)
    kkal_breakfast = models.IntegerField('Лимит на завтрак', default=0)
    kkal_dinner = models.IntegerField('Лимит на обед', default=0)
    kkal_sup = models.IntegerField('Лимит на ужин', default=0)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.user.id)])

    def kkal_limit_breakfast(self):
        self.kkal_breakfast = self.kkal * 0.3
        return self.kkal_breakfast

    def kkal_limit_dinner(self):
        self.kkal_dinner = self.kkal * 0.4
        return self.kkal_dinner

    def kkal_limit_sup(self):
        self.kkal_sup = self.kkal * 0.3
        return self.kkal_sup

    def __str__(self):
        return f'{self.id} -> {self.name}'

    def calculate_kkal(self):
        # if self.kkal == None or self.kkal == '' or self.kkal == 0:
        self.kkal = (88.362 + (13.97 * self.weight) + (4.799 * self.height) - (5.677 * self.age))
        return self.kkal

    def kkal_limit_variant(self):
        if self.kkal_limit_var == '1':
            self.kkal_limit_var = self.kkal * 0.8
        if self.kkal_limit_var == '2':
            self.kkal_limit_var = self.kkal
        if self.kkal_limit_var == '3':
            self.kkal_limit_var = self.kkal * 1.2
        return self.kkal_limit_var


# 1=похудеть; 2=сохранить вес; 3=набрать вес


@receiver(pre_save, sender=Profile)
def pre_save(sender, instance, **kwargs):
    sender.calculate_kkal(instance)


DAYS_OF_WEEK = (
    ('1', _('Monday')),
    ('2', _('Tuesday')),
    ('3', _('Wednesday')),
    ('4', _('Thursday')),
    ('5', _('Friday')),
    ('6', _('Saturday')),
    ('7', _('Sunday')),
)


class Day_of_week(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='profile_days')
    type = models.CharField('Day of week', max_length=25, choices=DAYS_OF_WEEK)
    dishes = models.ManyToManyField('Dishes', related_name='dishes', max_length=3)

    class Meta:
        verbose_name = 'Day'
        verbose_name_plural = 'Days'
        unique_together = ('profile', 'type')

    def __str__(self):
        return f'{self.id} -> {self.get_type_display()}'
