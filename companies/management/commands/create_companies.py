from random import getrandbits

from mimesis import Generic, Address
from django.core.management import BaseCommand
from mimesis.builtins import RussiaSpecProvider

from catalogs.types_of_companies.models import TypeOfCompany
from companies.models import Company


def generate_address():
    address = Address("ru")
    country = address.country()
    region = address.federal_subject()
    city = address.city()
    address = address.address()
    return f"{country}, {region}, {city}, {address}"


class Command(BaseCommand):
    def handle(self, *args, **options):
        mock = Generic("ru")
        mock.add_provider(RussiaSpecProvider)
        for _ in range(10):
            Company.objects.create(
                is_customer=getrandbits(1),
                is_transporter=getrandbits(1),
                type_of_company=TypeOfCompany.objects.order_by("?").first(),
                name=mock.business.company(),
                inn=mock.russia_provider.inn(),
                address=generate_address()
            )