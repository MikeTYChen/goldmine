from django.contrib import admin
from .models import Company, Job, Location


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'lat', 'long')
    fields = ('address','lat', 'long')

admin.site.register(Job)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)