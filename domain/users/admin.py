from django.contrib import admin

# Register your models here.
from .models.Profile import Profile

admin.site.register(Profile)
