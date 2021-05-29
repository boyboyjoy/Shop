from django.forms import ModelForm
from database_view.models.worker_model import WorkerModel


class WorkerForm(ModelForm):
    class Meta:
        model = WorkerModel
        fields = ('position_id', 'department_id', 'surname', 'name', 'second_name', 'phone')
