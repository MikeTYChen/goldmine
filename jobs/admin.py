from django.contrib import admin

from .models import Company, Job, Location

# Register your models here.
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Location)