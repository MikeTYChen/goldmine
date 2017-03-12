from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, mixins, permissions, status, viewsets

from . import models, serializers, scraper

class JobViewSet(viewsets.ModelViewSet):
    model = models.Job
    queryset = models.Job.objects
    serializer_class = serializers.JobSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    model = models.Company
    queryset = models.Company.objects
    serializer_class = serializers.CompanySerializer

def scrape(self):
  print("Scraping Data")
  company_info = scraper.load_scraped_data()
  print(company_info)
  for company in company_info:
    print(company)
    location = models.Location.objects.get_or_create(address=company[1],lat=company[2],long=company[3])[0]
    company = models.Company.objects.get_or_create(name=company[0], location=location)
  html = "<html><body>Scraping Data...</body></html>"
  return HttpResponse(html)