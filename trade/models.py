from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#     phone_number = models.CharField(max_length=10, blank=True)
#     location = models.CharField(max_length=30, blank=True)

class CanonicalGood(models.Model):
    name = models.CharField(
        max_length=63, unique=True)
    slug = models.SlugField(
        max_length=63, unique=True)

    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.ForeignKey(CanonicalGood)
    description = models.TextField(null=True, blank=True)
    modified = models.DateField(
        auto_now=True)
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True
        )
    user = models.ForeignKey(User, null=True)


class UserInfo(models.Model):
    user = models.ForeignKey(User)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)

class Need(models.Model):
    name = models.ForeignKey(CanonicalGood)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, null=True)
    modified = models.DateField(
        auto_now=True)
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        default=0
        )

class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TransactionUserGood(models.Model):
    transaction = models.ForeignKey(Transaction)
    user = models.ForeignKey(User)
    good = models.ForeignKey(Good)
    need = models.ForeignKey(Need)
