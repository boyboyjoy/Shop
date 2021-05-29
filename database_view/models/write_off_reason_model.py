from django.db import models


class WriteOffReasonModel(models.Model):
    reason_id = models.AutoField(primary_key=True)
    write_off_reason = models.CharField(max_length=50)

    def __str__(self):
        return self.write_off_reason
