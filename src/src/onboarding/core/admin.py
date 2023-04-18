from django.contrib import admin

from .models import OfficeMap


class OfficeMapAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "photo")


admin.site.register(OfficeMap, OfficeMapAdmin)