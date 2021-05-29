import datetime
from django.core.exceptions import ValidationError
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

    def clean_count(self):
        if int(self.cleaned_data.get('count')) > 0:
            return self.cleaned_data.get('count')
        raise ValidationError('Количество товара должно быть больше 0')

    def clean_date(self):
        if self.cleaned_data.get('date').date() <= datetime.datetime.now().date():
            return self.cleaned_data.get('date')
        raise ValidationError('Дата списания не может быть позже сегодняшего дня')
