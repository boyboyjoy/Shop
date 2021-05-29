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
