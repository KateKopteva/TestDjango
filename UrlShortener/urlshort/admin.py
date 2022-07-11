from django.contrib import admin
from .models import *

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at', 'long_url')
    list_filter = ('created_at',)