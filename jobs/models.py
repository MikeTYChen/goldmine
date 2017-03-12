from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
  name = models.CharField(max_length=100)
  summary = models.TextField(null=True)
  description = models.TextField(null=True)
  logo = models.URLField(null=True)
  url = models.URLField(null=True)
  location = models.ForeignKey('Location', blank=True, null=True, related_name="companies")


class Location(models.Model):
  address = models.CharField(max_length=150, blank=True, null=True)
  lat = models.FloatField(blank=True, null=True)
  long = models.FloatField(blank=True, null=True)

  def __str__(self):
    if self.address:
      return self.address
    else:
      return ''
