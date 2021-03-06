from django.forms import ModelForm, ValidationError
from database_view.models.client_model import ClientModel


class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ('surname', 'name', 'second_name', 'phone')
        labels = {'name': 'имя', 'surname': 'фамилия', 'second_name': 'отчество', 'phone': 'телефон'}

    def clean_name(self):
        if str(self.cleaned_data.get('name')).isalpha():
            return self.cleaned_data.get('name')
        raise ValidationError('Имя должно содержать только буквы')

    def clean_surname(self):
        if str(self.cleaned_data.get('surname')).isalpha():
            return self.cleaned_data.get('surname')
        raise ValidationError('Фамилия должна содержать только буквы')

    def clean_phone(self):
        if str(self.cleaned_data.get('phone')).isdigit() \
                and str(self.cleaned_data.get('phone')).__len__() == 11:
            return self.cleaned_data.get('phone')
        raise ValidationError('Номер должен состоять только из цифр и быть длиной 11 цифр')

    def clean_second_name(self):
        if str(self.cleaned_data.get('second_name')).isalpha():
            return self.cleaned_data.get('second_name')
        raise ValidationError('Отчество должно содержать только буквы')
