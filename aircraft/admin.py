from django.contrib import admin

from .models import Aircraft


class AircraftAdmin(admin.ModelAdmin):
    pass


admin.site.register(Aircraft, AircraftAdmin)
