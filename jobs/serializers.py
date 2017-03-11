from rest_framework import serializers
from . import models


class JobSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Job
    fields = ('id', 'title', 'link', 'posted_on', 'company', 'description')


class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Company
    fields = ('id', 'name', 'url')


class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Location
    fields = ('id', 'name', 'url')