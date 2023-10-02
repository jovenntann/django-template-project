from django.test import TestCase

from domain.users.tests.utils.utils import create_user_test

from domain.stores.models import Store

from ...models import Category
from ...models import Product

from ...services.service_Product import get_products, get_product_by_id, delete_product, \
    create_product, update_product


# Create your tests here.
class ServiceProductGetProductsTestCase(TestCase):

    def test_should_be_able_to_get_all_products(self):
        """Should return all products"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        category = Category.objects.create(
            name="Phones",
            description="All kind of phones"
        )
        product = Product.objects.create(
            store=store,
            title="iPhone",
            description="Best Phone"
        )
        product.categories.set([category])
        product.save()

        product_objects = get_products()
        expected_values = {
            'id': product.id,
            'store': store.id,
            'categories': product.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        actual_values = {
            'id': product_objects[0].id,
            'store': product_objects[0].store.id,
            'categories': product_objects[0].categories,
            'title': product_objects[0].title,
            'description': product_objects[0].description,
            'created_at': product_objects[0].created_at,
            'updated_at': product_objects[0].updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceProductGetProductByIdTestCase(TestCase):

    def test_should_return_none_if_product_id_do_not_exist(self):
        """Should return None if category id do not exist"""
        not_existing_product_id = 9999999999
        product = get_product_by_id(not_existing_product_id)
        self.assertIsNone(product)

    def test_should_be_able_to_get_product_by_id(self):
        """Should be able to get product object by id"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        category = Category.objects.create(
            name="Phones",
            description="All kind of phones"
        )
        product = Product.objects.create(
            store=store,
            title="iPhone",
            description="Best Phone"
        )
        product.categories.set([category])
        product.save()

        product_object_by_id = get_product_by_id(product.id)
        expected_values = {
            'id': product.id,
            'store': store.id,
            'categories': product.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        actual_values = {
            'id': product_object_by_id.id,
            'store': product_object_by_id.store.id,
            'categories': product_object_by_id.categories,
            'title': product_object_by_id.title,
            'description': product_object_by_id.description,
            'created_at': product_object_by_id.created_at,
            'updated_at': product_object_by_id.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceProductDeleteProductByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_product(self):
        """Should be able to delete product by object"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        category = Category.objects.create(
            name="Phones",
            description="All kind of phones"
        )
        product = Product.objects.create(
            store=store,
            title="iPhone",
            description="Best Phone"
        )
        product.categories.set([category])
        product.save()

        deleted_product_object = delete_product(product)
        self.assertEqual(product, deleted_product_object)


class ServiceProductCreateProductTestCase(TestCase):

    def test_should_be_able_create_product(self):
        """Should be able to create a product"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        category = Category.objects.create(
            name="Phones",
            description="All kind of phones"
        )
        product = create_product(
            store,
            [category.id],
            'iPhone',
            'Best Phone'
        )
        expected_values = {
            'id': product.id,
            'store': store.id,
            'categories': product.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        actual_values = {
            'id': product.id,
            'store': product.store.id,
            'categories': product.categories,
            'title': product.title,
            'description': product.description,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceProductUpdateProductByObjectTestCase(TestCase):

    def test_should_be_able_update_product(self):
        """Should be able to update a product"""
        user = create_user_test()
        store = Store.objects.create(
            user=user,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        category = Category.objects.create(
            name="Phones",
            description="All kind of phones"
        )
        product = Product.objects.create(
            store=store,
            title="iPhone",
            description="Best Phone"
        )
        product.categories.set([category])
        product.save()

        update_product_object = update_product(
            product,
            store,
            [category.id],
            'iPhone',
            'Best Phone'
        )

        expected_values = {
            'id': product.id,
            'store': store.id,
            'categories': product.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product.created_at,
            'updated_at': product.updated_at
        }
        actual_values = {
            'id': update_product_object.id,
            'store': update_product_object.store.id,
            'categories': update_product_object.categories,
            'title': update_product_object.title,
            'description': update_product_object.description,
            'created_at': update_product_object.created_at,
            'updated_at': update_product_object.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)
