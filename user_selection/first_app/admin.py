from django.contrib import admin

# Register your models here.

from . import models


class FamilyAdmin(admin.ModelAdmin):
    list_display = ["first_name", "second_name", ]


admin.site.register(models.Family, FamilyAdmin)
