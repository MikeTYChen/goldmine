from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
  lng = serializers.SerializerMethodField()
  lat = serializers.SerializerMethodField()

  def get_lng(self, obj):
    if obj.location:
      return obj.location.long
    return ''

  def get_lat(self, obj):
    if obj.location:
      return obj.location.lat
    return ''

  class Meta:
    model = models.Company
    fields = ('id', 'name', 'url', 'logo', 'lng', 'lat')


class JobSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Job
    fields = ('id', 'title', 'link', 'posted_on', 'company', 'description')
