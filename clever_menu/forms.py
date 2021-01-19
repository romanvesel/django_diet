from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'name', 'age', 'height', 'weight', 'kkal', 'kkal_limit_var']