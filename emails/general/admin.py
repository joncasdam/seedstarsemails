# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(Person, PersonAdmin)