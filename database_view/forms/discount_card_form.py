from django.core.exceptions import ValidationError
from django.forms import ModelForm
from database_view.models.discount_card_model import DiscountCardModel


class DiscountCardForm(ModelForm):
    class Meta:
        model = DiscountCardModel
        fields = ('client_id', 'discount_value')
        labels = {'client_id': 'клиент', 'discount_value': 'размер скидки'}

    def clean_discount_value(self):
        if 0 < float(self.cleaned_data.get('discount_value')) < 100:
            return self.cleaned_data.get('discount_value')
        raise ValidationError('Размер скидки должен быть меньше 100 и больше 0 и состоять только из чисел')
