from django.contrib import admin
from .models import Excursion


class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at', 'name')


admin.site.register(Excursion, ExcursionAdmin)
