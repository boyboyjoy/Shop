from django.db import models
from django.utils import timezone
from database_view.models.product_model import ProductModel
from database_view.models.worker_model import WorkerModel
from .write_off_reason_model import WriteOffReasonModel


class WriteOffProductModel(models.Model):
    write_off_product_id = models.AutoField(primary_key=True)
    worker_id = models.ForeignKey(WorkerModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    reason_id = models.ForeignKey(WriteOffReasonModel, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now=timezone.now)