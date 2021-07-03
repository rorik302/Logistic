from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField("В архиве", default=False)

    class Meta:
        abstract = True
