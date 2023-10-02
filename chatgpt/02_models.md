---
#### domain/commons/models/__init__.py
```
from .Base import BaseModel

```

#### domain/commons/models/Base.py
```
from django.db import models

import logging
logger = logging.getLogger(__name__)


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
```

#### domain/users/models/__init__.py
```
from .Profile import Profile
from .Receiver import *

```

#### domain/users/models/Profile.py
```
from django.db import models
from domain.commons.models.Base import BaseModel
from django.contrib.auth.models import User

import logging

logger = logging.getLogger(__name__)


class Profile(BaseModel):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):  # pragma: no cover
        return self.user.username

```

#### domain/stores/models/__init__.py
```
from .Store import Store

```

#### domain/stores/models/Store.py
```
from django.db import models
from domain.commons.models.Base import BaseModel
from django.contrib.auth.models import User


import logging
logger = logging.getLogger(__name__)


class Store(BaseModel):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='stores', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def get_excerpt(self, char: int) -> str:
        return self.address[:char]

    def __str__(self):
        return self.name

```

#### domain/products/models/__init__.py
```
from .Product import Product
from .Category import Category

```

#### domain/products/models/Product.py
```
from django.db import models
from domain.commons.models.Base import BaseModel
from .Category import Category
from domain.stores.models import Store


import logging
logger = logging.getLogger(__name__)


class Product(BaseModel):

    id = models.AutoField(primary_key=True)
    # Relationship: Many-to-one
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    # Relationship: Many-to-many
    categories = models.ManyToManyField(Category, related_name="products", blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):  # pragma: no cover
        return self.title
```

#### domain/products/models/Category.py
```
from django.db import models
from domain.commons.models.Base import BaseModel

import logging

logger = logging.getLogger(__name__)


class Category(BaseModel):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):  # pragma: no cover
        return self.name
```
