from django.contrib import admin

from search.models import Site, RequestSiteLog


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display  = ['name', 'url', 'created_at']


@admin.register(RequestSiteLog)
class RequestSiteLogAdmin(admin.ModelAdmin):
    list_display  = ['site', 'response', 'created_at']
