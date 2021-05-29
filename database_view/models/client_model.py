from django.db import models
from django.urls import reverse


class ClientModel(models.Model):
    client_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    second_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return " ".join([self.surname, self.name, self.second_name])