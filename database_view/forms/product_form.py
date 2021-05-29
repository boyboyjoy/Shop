from django.forms import ModelForm
from database_view.models.product_model import ProductModel


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = ('title', 'price', 'vendor_code', 'count')
