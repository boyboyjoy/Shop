from django.core.exceptions import ValidationError
from django.forms import ModelForm
from database_view.models.position_model import PositionModel


class PositionForm(ModelForm):
    class Meta:
        model = PositionModel
        fields = ('name', 'salary')
        labels = {'name': 'должность', 'salary': 'зарплата'}

    def clean_salary(self):
        if int(self.cleaned_data.get('salary')) > 0:
            return self.cleaned_data.get('salary')
        raise ValidationError('Зарплата должна быть больше 0')
