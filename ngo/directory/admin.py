from django.contrib import admin

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

admin.site.register(OrgDirectory, OrgDirectoryAdmin)