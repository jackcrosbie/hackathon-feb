from django.contrib import admin
from .models import OrgDirectory, Event, Location


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = (
        'name',
    )


class OrgDirectoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'work',
        'location',
        'summary',
        'website',
        'facebook',
        'instagram',
    )

    ordering = (
        'name',
    )


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'time',
        'date',
        'org',
        'location',
        'summary',
        'website',
    )

    ordering = (
        'org',
    )


admin.site.register(Location, LocationAdmin)
admin.site.register(OrgDirectory, OrgDirectoryAdmin)
admin.site.register(Event, EventAdmin)
