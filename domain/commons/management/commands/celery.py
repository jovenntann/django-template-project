# Library: celery (Auto Reload)

import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload

""" This is to automatically reload the Celery Service when the Django automatically reload during code update """


def restart_celery(*args, **kwargs):
    kill_worker_cmd = 'pkill -9 celery'
    subprocess.call(shlex.split(kill_worker_cmd))
    start_worker_cmd = 'celery -A project worker -l info'
    subprocess.call(shlex.split(start_worker_cmd))


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Starting celery worker with auto reload...')
        autoreload.run_with_reloader(restart_celery, args=None, kwargs=None)
