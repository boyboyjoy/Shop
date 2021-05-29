from django.forms import ModelForm
from database_view.models.department_model import DepartmentModel


class DepartmentForm(ModelForm):
    class Meta:
        model = DepartmentModel
        fields = ('name',)
        labels = {'name': 'название', }
