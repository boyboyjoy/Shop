from django.db import models
from database_view.models.department_model import DepartmentModel
from .position_model import PositionModel


class WorkerModel(models.Model):
    worker_id = models.AutoField(primary_key=True)
    position_id = models.ForeignKey(PositionModel, on_delete=models.CASCADE)
    department_id = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    second_name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return " ".join([self.surname, self.name, self.second_name])
