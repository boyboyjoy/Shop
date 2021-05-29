from django.forms import ModelForm
from database_view.models.worker_model import WorkerModel


class WorkerForm(ModelForm):
    class Meta:
        model = WorkerModel
        fields = ('position_id', 'department_id', 'surname', 'name', 'second_name', 'phone')
        labels = {'position_id': 'должность', 'department_id': 'отдел', 'surname': 'фамилия',
                  'name': 'имя', 'second_name': 'отчество', 'phone': 'контактный телефон'}
