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
