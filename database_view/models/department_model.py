from django.db import models


class DepartmentModel(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
