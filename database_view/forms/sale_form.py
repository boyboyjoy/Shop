from django.forms import ModelForm, DateTimeInput
from database_view.models.sale_model import SaleModel


class SaleForm(ModelForm):
    class Meta:
        model = SaleModel
        fields = ('worker_id', 'client_id', 'product_id', 'sale_cost', 'sale_date')
        labels = {'worker_id': 'работник', 'client_id': 'клиент', 'product_id': 'продукт',
                  'sale_cost': 'цена', 'sale_date': 'дата продажи'}
        widgets = {
            'sale_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
