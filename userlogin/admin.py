from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Details

# Register your models here.
admin.site.register(Details)
