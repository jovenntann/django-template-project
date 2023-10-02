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
