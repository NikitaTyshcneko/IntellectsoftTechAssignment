from django.contrib import admin
from intellectsoft_app import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Request)
admin.site.register(models.Operator)
