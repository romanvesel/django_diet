from django.contrib import admin
from .models import Day_of_week, Profile, Dishes


class DayOfWeekInline(admin.TabularInline):
    model = Day_of_week.dishes.through
    extra = 1


class DishesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kkal_of_dish', 'compose', 'recipe', 'kind_of_dish', 'img',)
    inlines = (DayOfWeekInline,)


class DayOfWeekAdmin(admin.ModelAdmin):
    model = Day_of_week
    list_display = ('id', 'profile', 'get_type_display')
    filter_horizontal = ('dishes',)


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('id', 'email', 'user', 'name', 'age')
    list_filter = ('email',)


admin.site.register(Day_of_week, DayOfWeekAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Dishes, DishesAdmin)
