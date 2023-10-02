from django.contrib import admin

# Register your models here.
from .models import Store

admin.site.site_header = 'Django Admin'
admin.site.site_title = 'Django Admin'
admin.site.index_title = 'Django Administration'


class StoreAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ('user', 'name')


admin.site.register(Store, StoreAdmin)

