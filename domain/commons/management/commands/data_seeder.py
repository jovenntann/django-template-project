import os
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from domain.users.models import Profile
from domain.stores.models import Store
from domain.products.models import Product, Category

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Seed data for the application'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10, help='Number of users to create')
        parser.add_argument('--stores', type=int, default=5, help='Number of stores per user')
        parser.add_argument('--categories', type=int, default=10, help='Number of categories to create')
        parser.add_argument('--products', type=int, default=5, help='Number of products per store')

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Seed Users and Profiles
        for _ in range(options['users']):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='testpassword123'
            )
            # Profile.objects.create(
            #     user=user,
            #     bio=fake.sentence(),
            #     location=fake.city(),
            #     birth_date=fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90)
            # )

        # Seed Categories
        categories = []
        for _ in range(options['categories']):
            category = Category.objects.create(
                name=fake.word(),
                description=fake.sentence()
            )
            categories.append(category)

        # Seed Stores and Products
        users = User.objects.all()
        for user in users:
            for _ in range(options['stores']):
                store = Store.objects.create(
                    user=user,
                    name=fake.company(),
                    contact_number=fake.phone_number()[:12],
                    address=fake.address()[:50],
                )
                for _ in range(options['products']):
                    product = Product.objects.create(
                        store=store,
                        title=fake.sentence(nb_words=3),
                        description=fake.sentence()
                    )
                    # Assign random categories to the product
                    product_categories = random.sample(categories, random.randint(1, len(categories)))
                    for category in product_categories:
                        product.categories.add(category)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
