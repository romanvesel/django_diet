from django import template
from ..models import Dishes, Profile, Day_of_week
from random import randint
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter
def get_random(day, profile_id):
    _profile = Profile.objects.get(id=profile_id)
    return f'{day.id} {_profile.id}'


@register.filter
def update_get_random(random):
    day_id, profile_id = random.split()
    day = Day_of_week.objects.get(id=day_id, profile=profile_id)
    dishes = day.dishes.all()
    try:
        return [dishes[randint(0, dishes.count() - 1)]]
    except ObjectDoesNotExist:
        return ['']


@register.filter
def make_tuple(value: str):
    return value.split()
