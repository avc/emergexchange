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

class UserInfoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = models.UserInfo
        fields = (
            'id',
            'user',
            'username',
            'address',
            'phone_number'
        )

class CanonicalGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CanonicalGood
        fields = (
            'id',
            'name',
            'slug',
        )

class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Need
        fields = (
            'id',
            'name',
            'detail',
            'modified',
            'value',
        )

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = (
            'id',
            'created_at',
            'updated_at',
        )

class TransactionUserGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TransactionUserGood
        fields = (
            'id',
            'transaction',
            'user',
            'good',
            'need',
        )
