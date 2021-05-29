from django.db import models


class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField()
    vendor_code = models.CharField(max_length=15, blank=False, null=False)
    count = models.IntegerField(null=False)

    def __str__(self):
        return self.title
