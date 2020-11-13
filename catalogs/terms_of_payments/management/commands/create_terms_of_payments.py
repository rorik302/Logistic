from random import choice, randint
from django.core.management import BaseCommand
from catalogs.terms_of_payments.models import Term


days_types = ["календарные", "банковские"]
reasons = ["по оригиналам документов", "по копиям документов"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(10):
            Term.objects.create(
                days_count=randint(1, 60),
                days_type=choice(days_types),
                reason=choice(reasons)
            )
