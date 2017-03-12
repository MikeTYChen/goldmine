from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
  lng = serializers.SerializerMethodField()
  lat = serializers.SerializerMethodField()
  address = serializers.SerializerMethodField()

  def get_address(self, obj):
    if obj.address:
      return obj.location.address
    return ''

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
    fields = ('id', 'name', 'summary', 'description', 'url', 'logo', 'lng', 'lat', 'address')
