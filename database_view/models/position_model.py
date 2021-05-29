from django.db import models


class PositionModel(models.Model):
    position_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    salary = models.FloatField()

    def __str__(self):
        return self.name
