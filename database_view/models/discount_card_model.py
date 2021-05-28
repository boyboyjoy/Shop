from django.db import models
from database_view.models.client_model import ClientModel


class DiscountCardModel(models.Model):
    card_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    discount_value = models.FloatField(null=False)
