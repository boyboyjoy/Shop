from django.forms import ModelForm, ValidationError
from database_view.models.client_model import ClientModel


class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ('name', 'surname', 'phone')
        labels = {'name': 'имя', 'surname': 'фамилия', 'phone': 'телефон'}

    def clean_name(self):
        if str(self.cleaned_data.get('name')).isalpha():
            return self.cleaned_data.get('name')
        else:
            raise ValidationError('Имя должно содержать только буквы')

    def clean_surname(self):
        if str(self.cleaned_data.get('surname')).isalpha():
            return self.cleaned_data.get('surname')
        else:
            raise ValidationError('Фамилия должна содержать только буквы')

    def clean_phone(self):
        if str(self.cleaned_data.get('phone')).isdigit() \
                and str(self.cleaned_data.get('phone')).__len__() == 11:
            return self.cleaned_data.get('phone')
        else:
            raise ValidationError('Номер должен состоять только из цифр и быть длиной 11 цифр')
