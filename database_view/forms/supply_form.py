import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateTimeInput
from database_view.models.supply_model import SupplyModel


class SupplyForm(ModelForm):
    class Meta:
        model = SupplyModel
        fields = ('product_id', 'provider_id', 'count', 'supply_date')
        labels = {'product_id': 'продукт', 'provider_id': 'поставщик', 'count': 'количество',
                  'supply_date': 'дата поставки'}
        widgets = {
            'supply_date': DateTimeInput(attrs={'type': 'date'}),
        }

    def clean_count(self):
        if int(self.cleaned_data.get('count')) > 0:
            return self.cleaned_data.get('count')
        raise ValidationError('Количество в поставке должно быть больше 0')

    def clean_supply_date(self):
        if self.cleaned_data.get('supply_date').date() <= datetime.datetime.now().date():
            return self.cleaned_data.get('supply_date')
        raise ValidationError('Дата поставки должна быть не позднее сегодняшнего дня')
