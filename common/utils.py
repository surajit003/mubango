from address.models import Address, Locality, State, Country


def generate_country_data_for_testing():
    country = Country.objects.create(name="Kenya", code="KE")
    state = State.objects.create(name="Nairobi", country=country)
    locality = Locality.objects.create(name="USIU", state=state)
    address = Address.objects.create(
        street_number="USIU Road Thika road",
        locality=locality,
        raw="USIU road",
        latitude="-1.2211537",
        longitude="36.88339089999999",
    )
    return address
