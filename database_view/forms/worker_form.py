from django.core.exceptions import ValidationError
from django.forms import ModelForm
from database_view.models.worker_model import WorkerModel


class WorkerForm(ModelForm):
    class Meta:
        model = WorkerModel
        fields = ('position_id', 'department_id', 'surname', 'name', 'second_name', 'phone')
        labels = {'position_id': 'должность', 'department_id': 'отдел', 'surname': 'фамилия',
                  'name': 'имя', 'second_name': 'отчество', 'phone': 'контактный телефон'}

    def clean_name(self):
        if str(self.cleaned_data.get('name')).isalpha():
            return self.cleaned_data.get('name')
        raise ValidationError('Имя должно содержать только буквы')

    def clean_surname(self):
        if str(self.cleaned_data.get('surname')).isalpha():
            return self.cleaned_data.get('surname')
        raise ValidationError('Фамилия должна содержать только буквы')

    def clean_second_name(self):
        if str(self.cleaned_data.get('second_name')).isalpha():
            return self.cleaned_data.get('second_name')
        raise ValidationError('Отчество должно содержать только буквы')

    def clean_phone(self):
        if str(self.cleaned_data.get('phone')).isdigit() \
                and str(self.cleaned_data.get('phone')).__len__() == 11:
            return self.cleaned_data.get('phone')
        raise ValidationError('Номер должен состоять только из цифр и быть длиной 11 цифр')