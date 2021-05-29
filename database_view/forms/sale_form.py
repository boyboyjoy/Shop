from django.forms import ModelForm
from database_view.models.sale_model import SaleModel


class SaleForm(ModelForm):
    class Meta:
        model = SaleModel
        fields = ('worker_id', 'client_id', 'product_id', 'sale_cost', 'sale_date')
