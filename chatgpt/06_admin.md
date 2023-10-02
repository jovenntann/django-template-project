---
#### domain/products/admin.py
```
from django.contrib import admin

# Register your models here.
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)

```

#### domain/stores/admin.py
```
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

```

#### domain/users/admin.py
```
from django.contrib import admin

# Register your models here.
from .models.Profile import Profile

admin.site.register(Profile)
```