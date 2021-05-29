from django.db import models
from django.utils import timezone
from database_view.models.product_model import ProductModel
from database_view.models.provider_model import ProviderModel


class SupplyModel(models.Model):
    supply_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    provider_id = models.ForeignKey(ProviderModel, on_delete=models.CASCADE)
    count = models.IntegerField()
    supply_date = models.DateTimeField(default=timezone.now)