from django.forms import ModelForm
from database_view.models.supply_model import SupplyModel


class SupplyForm(ModelForm):
    class Meta:
        model = SupplyModel
        fields = ('product_id', 'provider_id', 'count', 'supply_date')
