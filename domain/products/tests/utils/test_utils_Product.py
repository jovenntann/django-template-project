from domain.products.models import Product


def create_product_test(store, category):
    product = Product.objects.create(
        store=store,
        title='iPhone',
        description="Best Phone"
    )
    product.categories.set([category])
    product.save()
    return product
