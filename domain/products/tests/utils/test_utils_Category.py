from domain.products.models import Category


def create_category_test():
    category = Category.objects.create(
        name="Phones",
        description="All kind of phones"
    )
    return category
