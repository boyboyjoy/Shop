from django.core.exceptions import ValidationError
from django.forms import ModelForm
from database_view.models.product_model import ProductModel


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = ('title', 'price', 'vendor_code', 'count')
        labels = {'title': 'товар', 'price': 'цена', 'vendor_code': 'штрих-код', 'count': 'количество'}

    def clean_price(self):
        if int(self.cleaned_data.get('price')) > 0:
            return self.cleaned_data.get('price')
        raise ValidationError('Цена должна быть больше 0')

    def clean_count(self):
        if int(self.cleaned_data.get('count')) > 0:
            return self.cleaned_data.get('count')
        raise ValidationError('Количество товара должно быть положительным значением')

    def clean_vendor_code(self):
        if str(self.cleaned_data.get('vendor_code')).isdigit() and \
                str(self.cleaned_data.get('vendor_code')).__len__() == 13:
            return self.cleaned_data.get('vendor_code')
        raise ValidationError('Штрих код должен быть длиной в 13 символов и состоять из цифр')
