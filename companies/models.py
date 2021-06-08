from django.db import models

from core.models import BaseModel


class CompanyType(BaseModel):
    name_short = models.CharField('Сокращенное наименование', max_length=255)
    name_full = models.CharField('Полное наименование', max_length=255)

    def __str__(self):
        return self.name_short

    class Meta:
        db_table = 'company_types'
