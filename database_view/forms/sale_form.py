import datetime

from django.core.exceptions import ValidationError
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

    def clean_sale_cost(self):
        if int(self.cleaned_data.get('sale_cost')) > 0:
            return self.cleaned_data.get('sale_cost')
        raise ValidationError('Сумма продажи должна быть больше 0')

    def clean_sale_date(self):
        if self.cleaned_data.get('sale_date').date() <= datetime.datetime.now().date():
            return self.cleaned_data.get('sale_date')
        raise ValidationError('Дата продажи не может быть позже текущего дня')
