from django.db import models

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

class Transaction(models.Model):
    created_at = models.DateField()

class Need(models.Model):
    name = models.ForeignKey(CanonicalGood)
    detail = models.TextField()
    modified = models.DateField(
        auto_now=True)
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2)
