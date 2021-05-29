from django.forms import ModelForm
from database_view.models.write_off_reason_model import WriteOffReasonModel


class WriteOffReasonForm(ModelForm):
    class Meta:
        model = WriteOffReasonModel
        fields = ('write_off_reason', )
        labels = {'write_off_reason': 'причина списания', }
