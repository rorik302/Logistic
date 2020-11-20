from django.core.management import BaseCommand
from mimesis import Generic, Datetime, Address
from mimesis.builtins import RussiaSpecProvider

from companies.models import Company
from requests_app.models import Request


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
            Request.objects.create(
                number=f"{mock.numbers.integer_number(start=1)}/2020",
                loading_date=Datetime().date(start=2020, end=2020),
                loading_address=generate_address(),
                unloading_date=Datetime().date(start=2020, end=2020),
                unloading_address=generate_address(),
                customer=Company.objects.filter(is_customer=True).order_by('?').first(),
                transporter=Company.objects.filter(is_transporter=True).order_by('?').first(),
                customer_rate=mock.numbers.decimal_number(start=5000),
                transporter_rate=mock.numbers.decimal_number(start=5000)
            )