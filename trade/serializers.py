from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

class GoodSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = models.Good
        fields = (
            'id',
            'name',
            'description',
            'modified',
            'value',
        )
