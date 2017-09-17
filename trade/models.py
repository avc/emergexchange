from django.db import models
from django.contrib.auth.models import User

class CanonicalGood(models.Model):
    name = models.CharField(
        max_length=63, unique=True)
    slug = models.SlugField(
        max_length=63, unique=True)

class Good(models.Model):
    name = models.ForeignKey(CanonicalGood)
    description = models.TextField()
    modified = models.DateField(
        auto_now=True)
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2)

class UserInfo(models.Model):
    user = models.ForeignKey(User, related_name='user-info')
    address = models.TextField()
    phone-number = models.CharField(max_length=10)
    

class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='transaction-user')


class Need(models.Model):
    name = models.ForeignKey(CanonicalGood)
    detail = models.TextField()
    modified = models.DateField(
        auto_now=True)
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2)
