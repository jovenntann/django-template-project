from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from domain.users.models import Profile
from domain.stores.models import Store
from domain.products.models import Product, Category


class Command(BaseCommand):
    help = 'Reset data for the application'

    def handle(self, *args, **options):
        self.stdout.write('Resetting data...')

        # Delete all objects from the models
        Product.objects.all().delete()
        Category.objects.all().delete()
        Store.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Data reset successfully!'))
