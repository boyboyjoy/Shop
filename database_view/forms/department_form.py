from django.core.exceptions import ValidationError
from django.forms import ModelForm
from database_view.models.department_model import DepartmentModel


class DepartmentForm(ModelForm):
    class Meta:
        model = DepartmentModel
        fields = ('name',)
        labels = {'name': 'название', }

    def clean_name(self):
        if str(self.cleaned_data.get('name')).isalpha():
            return self.cleaned_data.get('name')
        else:
            raise ValidationError('Название должно содержать только буквы')
