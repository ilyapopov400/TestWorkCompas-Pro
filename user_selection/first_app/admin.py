from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from . import models


class FamilyAdmin(admin.ModelAdmin):
    list_display = ["first_name", "second_name", ]


admin.site.register(models.Family, FamilyAdmin)

admin.site.register(models.User)
# admin.site.register(models.User, UserAdmin)   # не показывает CHOICES
