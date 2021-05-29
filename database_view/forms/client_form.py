from django.forms import ModelForm
from database_view.models.client_model import ClientModel

class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ('name', 'surname', 'phone')