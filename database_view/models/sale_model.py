from django.db import models
from django.utils import timezone
from database_view.models.client_model import ClientModel
from database_view.models.product_model import ProductModel
from database_view.models.worker_model import WorkerModel


class SaleModel(models.Model):
    sale_id = models.AutoField(primary_key=True)
    worker_id = models.ForeignKey(WorkerModel, on_delete=models.CASCADE)
    client_id = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    sale_cost = models.FloatField()
    sale_date = models.DateTimeField(auto_now=timezone.now)
