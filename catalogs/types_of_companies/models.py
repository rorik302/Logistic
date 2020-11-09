from django.db import models


class TypeOfCompany(models.Model):
    name_short = models.CharField(max_length=20)
    name_full = models.CharField(max_length=250)

    class Meta:
        db_table = "catalogs__types_of_companies"
