from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'email', 'name', 'age', 'height', 'weight', 'kkal', 'kkal_limit_var')
