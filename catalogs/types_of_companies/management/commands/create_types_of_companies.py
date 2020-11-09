from django.core.management import BaseCommand
from catalogs.types_of_companies.models import TypeOfCompany


types_of_companies = {
    "ПAO": "Публичное акционерное общество",
    "АО": "Акционерное общество",
    "ООО": "Общество с ограниченной ответственностью"
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for k, v in types_of_companies.items():
            TypeOfCompany.objects.create(
                name_short=k,
                name_full=v
            )
