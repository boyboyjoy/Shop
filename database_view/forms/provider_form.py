from django.forms import ModelForm
from django.forms import DateTimeInput
from database_view.models.provider_model import ProviderModel


class ProviderForm(ModelForm):
    class Meta:
        model = ProviderModel
        fields = ('name', 'phone', 'contract_expire')
        labels = {'name': 'фирма', 'phone': 'контактный телефон',
                  'contract_expire': 'дата истечения контракта'}
        widgets = {
            'contract_expire': DateTimeInput(attrs={'type': 'date'}),
        }
