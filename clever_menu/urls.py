import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from .views import IndexTemplateView, ProfileModelView, get_name_JSON, login_redirect, ProfileUpdateView, DishesView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('profile/<int:pk>/', ProfileModelView.as_view(), name='profile'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('dishes', DishesView.as_view(), name='dishes'),
    path('login_redirect', login_redirect, name='login_redirect'),
    path('get_name/<int:id>/', get_name_JSON),
    path('__debug__/', include(debug_toolbar.urls)),
]
