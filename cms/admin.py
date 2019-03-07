from django.contrib import admin
from cms import models

# Register your models here.

admin.site.register(models.Tags)
admin.site.register(models.Headline)
admin.site.register(models.AircraftModel)
admin.site.register(models.Aircraft)
admin.site.register(models.Airport)
admin.site.register(models.Flight)