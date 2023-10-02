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
