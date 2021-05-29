from django.forms import ModelForm, DateTimeInput
from database_view.models.write_off_product import WriteOffProductModel


class WriteOffProductForm(ModelForm):
    class Meta:
        model = WriteOffProductModel
        fields = ('worker_id', 'product_id', 'reason_id', 'count', 'date')
        labels = {'worker_id': 'работник', 'product_id': 'продукт', 'reason_id': 'причина списания',
                  'count': 'количество', 'date': 'дата списания'}
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'}),
        }
