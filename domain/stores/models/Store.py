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
