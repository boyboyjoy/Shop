import datetime

from django.core.exceptions import ValidationError
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

    def clean_phone(self):
        if str(self.cleaned_data.get('phone')).isdigit() \
                and str(self.cleaned_data.get('phone')).__len__() == 11:
            return self.cleaned_data.get('phone')
        raise ValidationError('Номер должен состоять только из цифр и быть длиной 11 цифр')

    def clean_contract_expire(self):
        if self.cleaned_data.get('contract_expire').date() > \
                (datetime.datetime.now().date() + datetime.timedelta(days=1)):
            return self.cleaned_data.get('contract_expire')
        raise ValidationError('Контракт должен истекать не ранее завтрашнего дня')
