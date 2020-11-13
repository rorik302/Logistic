from django.db import models

from catalogs.types_of_companies.models import TypeOfCompany


class Company(models.Model):
    is_customer = models.BooleanField("Заказчик", default=False)
    is_transporter = models.BooleanField("Перевозчик", default=False)
    type_of_company = models.ForeignKey(TypeOfCompany, on_delete=models.PROTECT)
    name = models.CharField("Наименование", max_length=100)
    inn = models.PositiveSmallIntegerField("ИНН")
    address = models.CharField("Адрес", max_length=200)

    class Meta:
        db_table = "companies"
