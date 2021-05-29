from django.forms import ModelForm
from database_view.models.provider_model import ProviderModel


class ProviderForm(ModelForm):
    class Meta:
        model = ProviderModel
        fields = ('name', 'phone', 'contract_expire')
