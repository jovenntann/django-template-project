from .Profile import Profile

from django.contrib.auth.models import User

# Method: Extending User with Profile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Celery: Tasks
from ..tasks.task_mailer import send_email_verification

import logging
logger = logging.getLogger(__name__)


"""
Django provides several built-in signals, such as pre_save, post_save, 
pre_delete, and post_delete, which are triggered by specific events 
occurring in the application, usually related to models. 
"""


@receiver(post_save, sender=User)
def create_profile_on_user_creation(sender, instance, created, **kwargs):
    if created:
        logging.info(sender)
        logger.info("@receiver.create_profile_on_user_creation -> create_user_profile")
        Profile.objects.create(user=instance)
        logger.info(f"created profile for username: {instance.username}")
        send_email_verification.delay(instance.email, 'Please verify your email')
        logger.info("task created: send_email_verification")
