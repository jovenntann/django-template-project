from domain.stores.models import Store


def create_store_test(user):
    store = Store.objects.create(
        user=user,
        name="Apple",
        contact_number="+1023456789",
        address="California"
    )
    return store
