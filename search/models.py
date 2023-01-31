from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField(max_length=120)
    page_search_name = models.CharField(max_length=70)
    param_search_name = models.CharField(max_length=70)
    card_class = models.CharField(max_length=250)
    title_class = models.CharField(max_length=250)
    anchor_class = models.CharField(max_length=250)
    description_class = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True)
    modified_at = models.DateTimeField(auto_now=True)


class RequestSiteLog(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    response = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
