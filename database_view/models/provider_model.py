from django.db import models


class ProviderModel(models.Model):
    provider_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12)
    name = models.CharField(max_length=50, null=False, blank=False)
    contract_expire = models.DateTimeField()
