import django
from django.contrib import admin
from .models import model_for_form

# Register your models here.
admin.site.register(model_for_form)
