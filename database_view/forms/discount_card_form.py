from django.forms import ModelForm
from database_view.models.discount_card_model import DiscountCardModel


class DiscountCardForm(ModelForm):
    class Meta:
        model = DiscountCardModel
        fields = ('client_id', 'discount_value')
        labels = {'client_id': 'клиент', 'discount_value': 'размер скидки'}
