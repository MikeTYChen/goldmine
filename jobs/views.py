from django.shortcuts import render

from rest_framework import generics, mixins, permissions, status, viewsets

from . import models, serializers

class JobViewSet(viewsets.ModelViewSet):
    model = models.Job
    queryset = models.Job.objects
    serializer_class = serializers.JobSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    model = models.Company
    queryset = models.Company.objects
    serializer_class = serializers.CompanySerializer


class LocationViewSet(viewsets.ModelViewSet):
    model = models.Location
    queryset = models.Location.objects
    serializer_class = serializers.LocationSerializer