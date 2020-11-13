from django.db import models


class Term(models.Model):
    days_count = models.PositiveSmallIntegerField("Кол-во дней")
    days_type = models.CharField("Тип дней", max_length=15)
    reason = models.CharField("Основание", max_length=100)

    class Meta:
        db_table = "catalogs__terms_of_payments"
