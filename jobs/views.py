from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, mixins, permissions, status, viewsets

from . import models, serializers, scraper


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
    location = models.Location.objects.get_or_create(address=company[1], lat=company[2], long=company[3])[0]
    company = models.Company.objects.get_or_create(name=company[0])
    company.location = location
    company.save()
  html = "<html><body>Scraping Data...</body></html>"
  return HttpResponse(html)

def add_company_info(self):
  company_info = scraper.load_company_info()
  for company in company_info:
    print(company)
    current_company = models.Company.objects.get_or_create(name=company['name'])[0]
    current_company.summary = company['short_description']
    current_company.description = company['description']
    current_company.url = company['company_url']
    current_company.logo = company['logo_url']
    current_company.save()
  html = "<html><body>Adding Company Data...</body></html>"
  return HttpResponse(html)