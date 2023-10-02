from django.test import TestCase

from ...models import Category

from ...services.service_Category import get_categories, get_category_by_id, \
    delete_category, create_category, update_category


# Create your tests here.
class ServiceCategoryGetCategoriesTestCase(TestCase):

    def test_should_be_able_to_get_all_categories(self):
        """Should return all categories"""
        category = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        categories = get_categories()
        expected_values = {
            'id': category.id,
            'name': 'Shoes',
            'description': 'All kind of shoes',
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }
        actual_values = {
            'id': categories[0].id,
            'name': categories[0].name,
            'description': categories[0].description,
            'created_at': categories[0].created_at,
            'updated_at': categories[0].updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceCategoryGetCategoryByIdTestCase(TestCase):

    def test_should_return_none_if_category_id_do_not_exist(self):
        """Should return None if category id do not exist"""
        Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        not_existing_category_id = 99
        category = get_category_by_id(not_existing_category_id)
        self.assertIsNone(category)

    def test_should_be_able_to_get_category_by_id(self):
        """Should be able to get category object by id"""
        category = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        category_by_id = get_category_by_id(category.id)
        expected_values = {
            'id': category.id,
            'name': 'Shoes',
            'description': 'All kind of shoes',
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }
        actual_values = {
            'id': category_by_id.id,
            'name': category_by_id.name,
            'description': category_by_id.description,
            'created_at': category_by_id.created_at,
            'updated_at': category_by_id.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceCategoryDeleteCategoryByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_category(self):
        """Should be able to delete user by object"""
        category = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        deleted_category = delete_category(category)
        self.assertEqual(category, deleted_category)


class ServiceCategoryCreateCategoryTestCase(TestCase):

    def test_should_be_able_create_category(self):
        """Should be able to create a category"""
        category = create_category('Shoes', 'All kind of shoes')
        expected_values = {
            'id': category.id,
            'name': 'Shoes',
            'description': 'All kind of shoes',
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }
        actual_values = {
            'id': category.id,
            'name': category.name,
            'description': category.description,
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)


class ServiceCategoryUpdateCategoryTestCase(TestCase):

    def test_should_be_able_to_update_category(self):
        """Should be able to update a category"""
        category = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        updated_category = update_category(
            category,
            name='Shirts',
            description='All kind of shirts'
        )
        expected_values = {
            'id': category.id,
            'name': 'Shirts',
            'description': 'All kind of shirts',
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }
        actual_values = {
            'id': updated_category.id,
            'name': updated_category.name,
            'description': updated_category.description,
            'created_at': updated_category.created_at,
            'updated_at': updated_category.updated_at
        }
        self.assertDictEqual(expected_values, actual_values)
