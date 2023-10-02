import re
import time

# Library: celery
from celery import shared_task

import logging
logger = logging.getLogger(__name__)


def check_if_valid_email(email: str) -> bool:

    # Make a regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    return False


@shared_task()
def send_email_verification(email_address: str, message: str) -> bool:

    is_valid_email = check_if_valid_email(email_address)

    if is_valid_email:
        logger.info(f"Sending email verification to {email_address} with message `{message}`")
        # Simulate delay on sending email
        # time.sleep(20)
        logger.info(f"Email successfully sent with message ID: 3b65fcf9-abf4-532f-b8b5-dcc18e5fee07")
        return True

    logger.info(f"{email_address} is not a valid email address")
    return False
