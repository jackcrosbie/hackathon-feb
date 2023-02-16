from django.contrib import admin


class PlayAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
    )

    ordering = (
        'name',
    )