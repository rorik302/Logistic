from django.db import models

from companies.models import Company


class Request(models.Model):
    number = models.CharField(max_length=20)
    loading_date = models.DateField()
    loading_address = models.CharField(max_length=250)
    unloading_date = models.DateField()
    unloading_address = models.CharField(max_length=250)
    customer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="customer")
    transporter = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="transporter")
    customer_rate = models.DecimalField(max_digits=10, decimal_places=2)
    transporter_rate = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "requests"
