from django.forms import ModelForm
from database_view.models.position_model import PositionModel


class PositionForm(ModelForm):
    class Meta:
        model = PositionModel
        fields = ('name', 'salary')
        labels = {'name': 'должность', 'salary': 'зарплата'}
