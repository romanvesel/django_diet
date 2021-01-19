from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Day_of_week, Dishes
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import generics, status, viewsets
from django.contrib.auth.decorators import login_required
from .serializers import ProfileSerializer
from .forms import ProfileForm


class IndexTemplateView(TemplateView):
    template_name = 'clever_menu/index.html'


class ProfileModelView(LoginRequiredMixin, DetailView):
    template_name = 'profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = instance = profile
        context['form'] = ProfileForm(instance=instance)
        return context


class DishesView(LoginRequiredMixin, TemplateView):
    template_name = 'day_of_week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['days_list'] = Day_of_week.objects.filter(profile=self.request.user.profile.pk)
        context['profile'] = self.request.user.profile
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = [
        'email', 'name', 'age', 'height', 'weight', 'kkal', 'kkal_limit_var'
    ]
    template_name = 'profile.html'

    def get_success_url(self):
        self.object.calculate_kkal()
        self.object.save()
        return self.object.get_absolute_url()


class ProfileModelAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


def get_name_JSON(request, id):
    name = Profile.objects.get(id=id).name
    data = {
        "name": name,
        "message": 'ОК',
        "status": 200
    }
    return JsonResponse(data, safe=True)


@login_required
def login_redirect(request):
    return redirect('profile', pk=request.user.pk)
